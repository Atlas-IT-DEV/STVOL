from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
from src.telegram_bot.handler.base_hendlers import BaseCommandHandler, _check, _cancel, _get_param, _inf_response
import requests
from src.database.models import Bouquet
from src.utils.custom_logging import setup_logging
log = setup_logging()


class EditBouquetHandler(BaseCommandHandler):
    CHOOSING, WAITING_FOR_PHOTO = range(2)

    FORMA = ("<pre>"
             "/edit_bouquet\n"
             "bouquet_id=ID\n"
             "name=Название\n"
             "price=Цена"
             "</pre>\n\n"
             "<code>BouquetID обязательный</code>\n"
             "<code>Name обязательный</code>\n"
             "<code>Price обязательный</code>\n\n")

    async def start(self, update: Update, context: CallbackContext) -> int:
        log.info("Command create_bouquet")
        try:
            if await self.check_authorized(update):
                instructions = (
                    "<b>Сначала напиши команду в формате:</b>\n"
                    f"{EditBouquetHandler.FORMA}"
                    "<i>Накосячил? Исправляй...</i>"
                )
                await update.message.reply_text(instructions, parse_mode='HTML')
                return self.CHOOSING
        except Exception as ex:
            log.exception(f"Failed method: {ex}")

    async def handle_message(self, update: Update, context: CallbackContext) -> int:
        log.debug(f"Handling message from user {update.message.from_user.id}")
        try:
            user_id = update.message.from_user.id
            text = update.message.text

            if text.startswith('/cancel'):
                return await self.cancel(update)

            if not text.startswith('/edit_bouquet'):
                instructions = (
                    "<b>Некорректный ввод команды. Используй команду в формате: </b>\n"
                    f"{EditBouquetHandler.FORMA}"
                    "<i>Повнимательнее?</i>"
                )
                await update.message.reply_text(instructions, parse_mode="HTML")
                return self.CHOOSING

            self.DATA[user_id] = _get_param(text, {
                "bouquet_id": "int",
                "name": "str",
                "price": "int"
            })

            if self.DATA[user_id]:
                log.debug(f"Current data for user {user_id}: {self.DATA[user_id]}")

                bouquet = requests.get(
                    f'http://{self.HOST}:{self.SERVER_PORT}/bouquets/id/{self.DATA[user_id]["bouquet_id"]}'
                )
                bouquet = Bouquet(**bouquet.json()).dict(by_alias=True)

                bouquet_data = {
                    "id": None,
                    "name": self.DATA.get(user_id, {}).get("name", bouquet.get("name")),
                    "price": self.DATA.get(user_id, {}).get("price", bouquet.get("price")),
                    "image_id": self.DATA.get(user_id, {}).get("image_id", bouquet.get("image_id"))
                }

                response = requests.put(
                    f'http://{self.HOST}:{self.SERVER_PORT}/bouquets/{self.DATA[user_id]["bouquet_id"]}',
                    json=bouquet_data
                )

                await _inf_response(update, response,
                                    "Букет изменен успешно.",
                                    f"Ошибка при изменении букета: \n{response.text}")

                del self.DATA[user_id]
                return ConversationHandler.END
            else:
                instructions = (
                    "<b>Некорректный ввод команды. Используй команду в формате: </b>\n"
                    f"{EditBouquetHandler.FORMA}"
                    "<i>Ну да, ну да, пошел я...</i>"
                )
                await update.message.reply_text(instructions, parse_mode="HTML")
                return self.CHOOSING
        except Exception as ex:
            log.exception(f"Failed to handle message: {ex}")
            await update.message.reply_text('<b>Произошла ошибка при обработке информации.</b>', parse_mode="HTML")
            return self.CHOOSING

    async def handle_photo(self, update: Update, context: CallbackContext) -> int:
        return ConversationHandler.END

    async def cancel(self, update: Update) -> int:
        return await _cancel(self, update)

    async def check_authorized(self, update: Update) -> bool:
        return await _check(update, self.AUTHORIZED_USERS)
