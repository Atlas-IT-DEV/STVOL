from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
from src.telegram_bot.handler.base_hendlers import BaseCommandHandler, _check, _cancel, _get_param, _inf_response
import requests
from src.database.models import User
from src.utils.custom_logging import setup_logging
log = setup_logging()


class CreateUserHandler(BaseCommandHandler):
    CHOOSING, WAITING_FOR_PHOTO = range(2)
    FORMA = ("<code>/create_user</code>\n"
             "<code>name=&lt;Имя&gt;</code>    <i>необязательный</i>\n"
             "<code>telegram_id=&lt;ID&gt;</code>    <i>обязательный</i>\n"
             "<code>phone=&lt;Номер телефона&gt;</code>    <i>обязательный</i>\n"
             "<code>count_bonus=&lt;Количество бонусов пользователя&gt;</code>    <i>необязательный</i>\n"
             "<code>referal=&lt;Пригласил ли пользователь друга? (True/False)&gt;</code>    <i>необязательный</i>\n\n")

    async def start(self, update: Update, context: CallbackContext) -> int:
        log.info("Command create_user")
        try:
            if await self.check_authorized(update):
                instructions = (
                    "<b>Напиши команду в формате:</b>\n"
                    f"{CreateUserHandler.FORMA}"
                    "<i>Хорошего дня :)</i>"
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

            if not text.startswith('/create_user'):
                instructions = (
                    "<b>Некорректный ввод команды. Используй команду в формате: </b>\n"
                    f"{CreateUserHandler.FORMA}"
                    "<i>Может передохнуть?</i>"
                )
                await update.message.reply_text(instructions, parse_mode="HTML")
                return self.CHOOSING

            self.DATA[user_id] = _get_param(text, {
                "name": "str",
                "telegram_id": "int",
                "phone": "str",
                "count_bonus": "int",
                "referal": "bool"
            })

            if user_id in self.DATA:
                log.debug(f"Current data for user {user_id}: {self.DATA[user_id]}")

                # Преобразуем данные в формат, соответствующий Pydantic модели
                user_data = User(**self.DATA[user_id]).dict(by_alias=True)

                response = requests.post(
                    f'http://{self.HOST}:{self.SERVER_PORT}/users/',
                    json=user_data
                )

                await _inf_response(update, response,
                                    "Пользователь создан успешно.",
                                    f"Ошибка при создании пользователя: \n{response.text}")

                del self.DATA[user_id]
                return ConversationHandler.END
            else:
                instructions = (
                    "<b>Некорректный ввод команды. Используй команду в формате: </b>\n"
                    f"{CreateUserHandler.FORMA}"
                    "<i>Попробуй еще раз.</i>"
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
