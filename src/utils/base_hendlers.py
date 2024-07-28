import os
from abc import ABC, abstractmethod
from telegram import Update
from src.utils.custom_logging import setup_logging
from telegram.ext import CallbackContext, ConversationHandler
from dotenv import load_dotenv
load_dotenv()
log = setup_logging()


class BaseCommandHandler(ABC):

    def __init__(self):
        self.DATA = {}
        self.HOST = os.getenv("HOST")
        self.PORT = int(os.getenv("PORT"))
        self.SERVER_PORT = int(os.getenv("SERVER_PORT"))
        self.AUTHORIZED_USERS = self.__list__(os.getenv("AUTHORIZED_USERS"))

    def __list__(self, s: str):
        return list(map(int, s.split(',')))

    @abstractmethod
    async def start(self, update: Update, context: CallbackContext) -> int:
        pass

    @abstractmethod
    async def handle_message(self, update: Update, context: CallbackContext) -> int:
        pass

    @abstractmethod
    async def handle_photo(self, update: Update, context: CallbackContext) -> int:
        pass


async def _check(update: Update, AUTHORIZED_USERS: list):
    user_id = update.message.from_user.id
    if user_id in AUTHORIZED_USERS:
        return True
    else:
        await update.message.reply_text('Тебе здесь не рады.')
        return False


async def _cancel(self, update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    if user_id in self.DATA:
        del self.DATA[user_id]
    await update.message.reply_text('Операция отменена.')
    log.info(f"Cancelled the operation.")
    return ConversationHandler.END


def _get_param(text, dir_params):
    args = text.split()
    for key, value in dir_params.items():
        for arg in args:
            if arg.startswith(f'{key}='):
                if value == "str":
                    dir_params[key] = arg[len(f'{key}='):]
                elif value == "int":
                    dir_params[key] = int(arg[len(f'{key}='):])
    return dir_params


async def _inf_response(update: Update, response, access: str, error: str):
    if response.status_code == 200:
        await update.message.reply_text(access)
    else:
        await update.message.reply_text(error)
