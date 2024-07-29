import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from src.telegram_bot.handler.bouquet_handlers.get_bouquets_list_handlers import GetBouquetsListHandler
from src.telegram_bot.handler.bouquet_handlers.create_bouquet_handlers import CreateBouquetHandler
from src.telegram_bot.handler.bouquet_handlers.edit_bouquet_handlers import EditBouquetHandler
from src.telegram_bot.handler.user_handlers.create_user_handlers import CreateUserHandler
from src.telegram_bot.handler.start_handlers import StartHandler
from src.telegram_bot.handler.user_handlers.get_users_list_handlers import GetUsersListHandler
from src.telegram_bot.handler.bouquet_handlers.del_bouquet_handlers import DelBouquetHandler
from src.telegram_bot.handler.user_handlers.edit_user_handlers import EditUserHandler
from src.telegram_bot.handler.user_handlers.del_user_handlers import DelUserHandler
from src.utils.custom_logging import setup_logging
from dotenv import load_dotenv
load_dotenv()
log = setup_logging()


class StvolBot:

    def __init__(self):
        self.TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

    @staticmethod
    def _application_add_handler(class_method, command_name):
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler(command_name, class_method.start)],
            states={
                class_method.CHOOSING: [
                    MessageHandler(filters.TEXT, class_method.handle_message)
                ],
                class_method.WAITING_FOR_PHOTO: [
                    MessageHandler(filters.ALL, class_method.handle_photo)
                ]
            },
            fallbacks=[CommandHandler('cancel', class_method.cancel)]
        )
        return conv_handler

    def start_bot(self):
        log.info("Started bot process")
        try:
            application = Application.builder().token(self.TELEGRAM_TOKEN).build()

            # Приветственное сообщение
            application.add_handler(self._application_add_handler(StartHandler(), 'start'))

            # Получение списка букетов
            application.add_handler(self._application_add_handler(GetBouquetsListHandler(), 'get_bouquets_list'))
            # Создание букета
            application.add_handler(self._application_add_handler(CreateBouquetHandler(), 'create_bouquet'))
            # Изменение букета
            application.add_handler(self._application_add_handler(EditBouquetHandler(), 'edit_bouquet'))
            # Удаление букета
            application.add_handler(self._application_add_handler(DelBouquetHandler(), 'del_bouquet'))

            # Получение списка пользователей
            application.add_handler(self._application_add_handler(GetUsersListHandler(), 'get_users_list'))
            # Изменение пользователя
            application.add_handler(self._application_add_handler(EditUserHandler(), 'edit_user'))
            # Создание пользователя
            application.add_handler(self._application_add_handler(CreateUserHandler(), 'create_user'))
            # Удаление букета
            application.add_handler(self._application_add_handler(DelUserHandler(), 'del_user'))

            log.info("Bot handler added. Starting polling")
            application.run_polling()
        except Exception as ex:
            log.error(f"{ex}")
        log.info("Bot startup complete")
