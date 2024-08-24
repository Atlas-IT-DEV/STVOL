import os
from src.utils.custom_logging import setup_logging
import pymysql

from config import Config

config = Config()
log = setup_logging()


class CreateSQL:

    def __init__(self):
        # Используем файл с расширением .sql
        self.path_to_sql = os.path.join(os.path.dirname(__file__), f"{config.__getattr__('DB')}.sql")
        self.connection = pymysql.connect(
            host=config.__getattr__("HOST"),
            db=config.__getattr__("DB"),
            port=int(config.__getattr__("DB_PORT")),
            user=config.__getattr__("DB_USER"),
            password=config.__getattr__("DB_PASSWORD"),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def read_sql(self):
        try:
            # Создание базы данных, если она не существует
            with self.connection.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{config.__getattr__('DB')}`")
                cursor.execute(f"USE `{config.__getattr__('DB')}`")

                # Открываем и выполняем SQL-скрипт
                with open(self.path_to_sql, "r", encoding="utf-8") as f:
                    sql_script = f.read()
                    # Выполнение всех запросов в файле
                    for statement in sql_script.split(';'):
                        if statement.strip():
                            cursor.execute(statement)

                self.connection.commit()
            log.info("Database was created successfully")
        except Exception as ex:
            log.warning("Error during SQL script execution")
        finally:
            self.connection.close()


if __name__ == "__main__":
    create_sql = CreateSQL()
    create_sql.read_sql()
