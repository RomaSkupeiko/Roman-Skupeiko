import csv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Функція для пошуку фільму за кодом у CSV-файлі
def find_movie_by_code(code):
    try:
        with open('data.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['код'].strip() == code.strip():
                    return row['nazva'], row['посилання']
    except FileNotFoundError:
        print("Файл data.csv не знайдено!")
    return None, None

# Обробка команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("👋 Вітаю! Надішліть код з TikTok, щоб отримати трейлер фільму.")

# Обробка текстових повідомлень
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_code = update.message.text.strip()
    movie_name, trailer_link = find_movie_by_code(user_code)

    if movie_name:
        response = f"🎬 *{movie_name}*\n🔗 [Дивитись трейлер]({trailer_link})"
    else:
        response = "❌ Фільм за цим кодом не знайдено. Спробуйте ще раз!"

    await update.message.reply_text(response, parse_mode='Markdown', disable_web_page_preview=True)

# Основна функція запуску бота
def main():
    TOKEN = "8101029747:AAE7fDC4a4YtDonmYEn1NzotM0BAb0agFlg"  # Вставте свій токен тут
    app = Application.builder().token(TOKEN).build()

    # Обробники команд і текстових повідомлень
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    print("✅ Бот запущено! Перевірте Telegram.")
    app.run_polling()

if __name__ == '__main__':
    main()
