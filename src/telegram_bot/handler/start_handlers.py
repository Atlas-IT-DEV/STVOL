from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
from src.utils.base_hendlers import BaseCommandHandler
from src.utils.base_hendlers import BaseCommandHandler, _check, _cancel
from src.utils.custom_logging import setup_logging
log = setup_logging()


class StartHandler(BaseCommandHandler):
    CHOOSING, WAITING_FOR_PHOTO = range(2)

    async def start(self, update: Update, context: CallbackContext) -> None:
        log.info("Command start")
        try:
            if await self.check_authorized(update, context):
                await update.message.reply_text('Доброго дня администратирования. Используй команды из меню.')
        except Exception as ex:
            log.error(f"Failed to send message: {e}")

    async def handle_message(self, update: Update, context: CallbackContext) -> int:
        pass

    async def handle_photo(self, update: Update, context: CallbackContext) -> int:
        pass

    async def cancel(self, update: Update, context: CallbackContext) -> int:
        return await _cancel(self, update, context)

    async def check_authorized(self, update: Update, context: CallbackContext) -> bool:
        return await _check(update, self.AUTHORIZED_USERS)
