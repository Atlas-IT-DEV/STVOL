import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext
from src.telegram_bot.handler.bouquet_handlers import CreateBouquetHandler
from src.telegram_bot.handler.start_handlers import StartHandler
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
            # Создание букета
            application.add_handler(self._application_add_handler(CreateBouquetHandler(), 'create_bouquet'))

            log.info("Bot handler added. Starting polling")
            application.run_polling()
        except Exception as ex:
            log.error(f"{ex}")
        log.info("Bot startup complete")
