import aiomysql
from pymysql.err import OperationalError


class Database:
    def __init__(self):
        self.connection = None
        self.connected = False

    async def connect(self):
        try:
            self.connection = await aiomysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='stvol',
                charset='utf8mb4',
                cursorclass=aiomysql.cursors.DictCursor
            )
            self.connected = True
            return True
        except OperationalError as e:
            self.connected = False
            return False

    async def check_and_reconnect(self):
        try:
            if not self.connected or self.connection is None:
                await self.connect()
            else:
                await self.connection.ping(reconnect=True)
        except OperationalError as e:
            await self.connect()

    async def execute_query(self, query, params=None):
        await self.check_and_reconnect()
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, params)
            await self.connection.commit()
            return cursor

    async def fetch_one(self, query, params=None):
        await self.check_and_reconnect()
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, params)
            return await cursor.fetchone()

    async def fetch_all(self, query, params=None):
        await self.check_and_reconnect()
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, params)
            return await cursor.fetchall()
