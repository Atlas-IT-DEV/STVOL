from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
from src.utils.base_hendlers import BaseCommandHandler, _check, _cancel, _get_param, _inf_response
from src.utils.custom_logging import setup_logging
import requests

log = setup_logging()


class CreateBouquetHandler(BaseCommandHandler):
    CHOOSING, WAITING_FOR_PHOTO = range(2)
    FORMA = ("<code>/create_bouquet</code>\n"
             "<code>name=&lt;Название&gt;</code>    <i>обязательный</i>\n"
             "<code>price=&lt;Цена&gt;</code>    <i>обязательный</i>\n\n")

    async def start(self, update: Update, context: CallbackContext) -> int:
        log.info("Command create_bouquet")
        try:
            if await self.check_authorized(update, context):
                instructions = (
                    "<b>Сначала напиши команду в формате:</b>\n"
                    f"{CreateBouquetHandler.FORMA}"
                    "<b>Затем отправь следующим сообщением изображение.</b>\n"
                    "<i>Не прикрепляй фото через File -&gt; через Photo or Video</i>"
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

            if not text.startswith('/create_bouquet'):
                instructions = (
                    "<b>Некорректный ввод команды. Используй команду в формате: </b>\n"
                    f"{CreateBouquetHandler.FORMA}"
                    "<i>Может передохнуть?</i>"
                )
                await update.message.reply_text(instructions, parse_mode="HTML")
                return self.CHOOSING

            self.DATA[user_id] = _get_param(text, {
                "name": "str",
                "price": "int"
            })

            if self.DATA[user_id]:
                await update.message.reply_text('<b>Отправь изображение букета.</b>', parse_mode="HTML")
                log.debug(f"Current data for user {user_id}: {self.DATA[user_id]}")
                return self.WAITING_FOR_PHOTO
            else:
                instructions = (
                    "<b>Некорректный ввод команды. Используй команду в формате: </b>\n"
                    f"{CreateBouquetHandler.FORMA}"
                    "<i>Попробуй еще раз?</i>"
                )
                await update.message.reply_text(instructions, parse_mode="HTML")
                return self.CHOOSING
        except Exception as ex:
            log.error(f"Failed to handle message: {ex}")
            await update.message.reply_text('<b>Произошла ошибка при обработке информации.</b>', parse_mode="HTML")
            return self.CHOOSING

    async def handle_photo(self, update: Update, context: CallbackContext) -> int:
        try:
            log.info(f"Handling photo from user {update.message.from_user.id}")
            user_id = update.message.from_user.id
            text = update.message.text

            if text and text.startswith('/cancel'):
                return await self.cancel(update, context)

            if user_id in self.DATA and update.message.photo:
                photo = update.message.photo[-1]
                file = await photo.get_file()
                file_data = await file.download_as_bytearray()

                bouquet_data = {
                    "bouquet_name": self.DATA.get(user_id, {}).get("name"),
                    "bouquet_price": self.DATA.get(user_id, {}).get("price")
                }

                response = requests.post(
                    f'http://{self.HOST}:{self.SERVER_PORT}/uploadfile/create_bouquet/',
                    files={'file': ('bouquet.jpg', file_data)},
                    data=bouquet_data
                )

                await _inf_response(update, response,
                                    "Букет создан успешно.",
                                    "Ошибка при создании букета.")

                del self.DATA[user_id]
                return ConversationHandler.END
            else:
                await update.message.reply_text('<b>Отправь изображение букета.</b>', parse_mode="HTML")
                return self.WAITING_FOR_PHOTO
        except Exception as ex:
            log.error(f"Failed to handle photo: {ex}")
            await update.message.reply_text('<b>Произошла ошибка при обработке фото.</b>', parse_mode="HTML")
            return self.WAITING_FOR_PHOTO

    async def cancel(self, update: Update, context: CallbackContext) -> int:
        return await _cancel(self, update, context)

    async def check_authorized(self, update: Update, context: CallbackContext) -> bool:
        return await _check(update, self.AUTHORIZED_USERS)
