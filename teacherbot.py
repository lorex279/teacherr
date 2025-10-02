# bot.py
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Отвечаем на команду /hello
    await update.message.reply_text("С Днём учителя ❤️")

def main() -> None:
    token = "8295260673:AAFRUzDSo5bN955Wo_zQNmkdHFq_1GryOVs"
    if not token:
        print("Ошибка: нужно задать переменную окружения TELEGRAM_BOT_TOKEN с токеном бота.")
        return

    # Создаём приложение (будет использовать polling)
    app = ApplicationBuilder().token(token).build()

    # Регистрируем обработчик команды /hello
    app.add_handler(CommandHandler("hello", hello_command))

    # Запуск long polling
    print("Бот запущен. Ожидаю команд...")
    app.run_polling()

if __name__ == "__main__":
    main()
