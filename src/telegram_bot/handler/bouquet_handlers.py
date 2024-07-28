from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
from src.utils.base_hendlers import BaseCommandHandler, _check, _cancel, _get_param, _inf_response
from src.utils.custom_logging import setup_logging
import requests
log = setup_logging()


class CreateBouquetHandler(BaseCommandHandler):
    CHOOSING, WAITING_FOR_PHOTO = range(2)


    async def start(self, update: Update, context: CallbackContext) -> int:
        log.info("Command create_bouquet")
        try:
            if await self.check_authorized(update, context):
                await update.message.reply_text(
                    'Сначала напиши команду в формате:'
                    ' (/create_bouquet bouquet_name=<Название> ... \n bouquet_price=<Цена>) \n'
                    'Затем отправь следующим сообщением изображение.\n'
                    '{Не прикрепляй фото через File -> через Photo or Video}'
                )
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
                await update.message.reply_text(
                    'Некорректный формат команды. Используй команду в формате:'
                    ' /create_bouquet bouquet_name=<Название> bouquet_price=<Цена>.')
                return self.CHOOSING

            self.DATA[user_id] = _get_param(text, {
                "bouquet_name": "str",
                "bouquet_price": "int"
            })

            if self.DATA[user_id]:
                await update.message.reply_text('Отправь изображение букета.')
                log.debug(f"Current data for user {user_id}: {self.DATA[user_id]}")
                return self.WAITING_FOR_PHOTO
            else:
                await update.message.reply_text(
                    'Некорректные данные. Убедись, что отправил данные в формате:'
                    ' /create_bouquet bouquet_name=<Название> bouquet_price=<Цена>.')
                return self.CHOOSING
        except Exception as ex:
            log.error(f"Failed to handle message: {ex}")
            await update.message.reply_text('Произошла ошибка при обработке информации.')
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

                for param in self.DATA[user_id]:
                    if param is None:
                        log.error("Bouquet_name or Bouquet_price is None")
                    else:
                        log.debug(f"Param: {param}")

                response = requests.post(
                    f'http://{self.HOST}:{self.SERVER_PORT}/uploadfile/create_bouquet',
                    files={'file': ('bouquet.jpg', file_data)},
                    data=self.DATA[user_id]
                )

                await _inf_response(update, response,
                                    "Букет создан успешно.",
                                    "Ошибка при создании букета.")

                del self.DATA[user_id]
                return ConversationHandler.END
            else:
                await update.message.reply_text('Отправь изображение букета.')
                return self.WAITING_FOR_PHOTO
        except Exception as ex:
            log.error(f"Failed to handle photo: {ex}")
            await update.message.reply_text('Произошла ошибка при обработке фото.')
            return self.WAITING_FOR_PHOTO

    async def cancel(self, update: Update, context: CallbackContext) -> int:
        return await _cancel(self, update, context)

    async def check_authorized(self, update: Update, context: CallbackContext) -> bool:
        return await _check(update, self.AUTHORIZED_USERS)

