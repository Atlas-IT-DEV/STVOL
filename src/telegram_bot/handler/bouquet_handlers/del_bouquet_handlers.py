from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
from src.utils.base_hendlers import BaseCommandHandler, _check, _cancel, _get_param, _inf_response
from src.utils.custom_logging import setup_logging
import requests

log = setup_logging()


class DelBouquetHandler(BaseCommandHandler):
    CHOOSING, WAITING_FOR_PHOTO = range(2)
    FORMA = ("<code>/del_bouquet</code>\n"
             "<code>bouquet_id=&lt;ID&gt;</code>    <i>обязательный</i>\n\n")

    async def start(self, update: Update, context: CallbackContext) -> int:
        log.info("Command del_bouquet")
        try:
            if await self.check_authorized(update, context):
                instructions = (
                    "<b>Напиши команду в формате:</b>\n"
                    f"{DelBouquetHandler.FORMA}"
                    "<i>Настроение во! :)</i>"
                )
                await update.message.reply_text(instructions, parse_mode='HTML')
                return self.CHOOSING
        except Exception as ex:
            log.error(f"Failed method: {ex}")

    async def handle_message(self, update: Update, context: CallbackContext) -> int:
        log.info(f"Handling message from user {update.message.from_user.id}")
        try:
            user_id = update.message.from_user.id
            text = update.message.text

            if text.startswith('/cancel'):
                return await self.cancel(update, context)

            if not text.startswith('/del_bouquet'):
                instructions = (
                    "<b>Некорректный ввод команды. Используй команду в формате: </b>\n"
                    f"{DelBouquetHandler.FORMA}"
                    "<i>Ты точно хочешь удалить этот букетик? :(</i>"
                )
                await update.message.reply_text(instructions, parse_mode="HTML")
                return self.CHOOSING

            self.DATA[user_id] = _get_param(text, {
                "bouquet_id": "int"
            })

            if self.DATA[user_id]:
                log.debug(f"Current data for user {user_id}: {self.DATA[user_id]}")

                response = requests.delete(
                    f'http://{self.HOST}:{self.SERVER_PORT}/bouquets/{self.DATA[user_id]["bouquet_id"]}',
                )

                await _inf_response(update, response,
                                    "Букет удален успешно.",
                                    "Ошибка при удалении букета.")

                del self.DATA[user_id]
                return ConversationHandler.END
            else:
                instructions = (
                    "<b>Некорректный ввод команды. Используй команду в формате: </b>\n"
                    f"{DelBouquetHandler.FORMA}"
                    "<i>Фух, давай попробуй еще разок.</i>"
                )
                await update.message.reply_text(instructions, parse_mode="HTML")
                return self.CHOOSING
        except Exception as ex:
            log.error(f"Failed to handle message: {ex}")
            await update.message.reply_text('<b>Произошла ошибка при обработке информации.</b>', parse_mode="HTML")
            return self.CHOOSING

    async def handle_photo(self, update: Update, context: CallbackContext) -> int:
        return ConversationHandler.END

    async def cancel(self, update: Update, context: CallbackContext) -> int:
        return await _cancel(self, update, context)

    async def check_authorized(self, update: Update, context: CallbackContext) -> bool:
        return await _check(update, self.AUTHORIZED_USERS)
