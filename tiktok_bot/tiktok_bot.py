import csv
import random
import telebot

TOKEN = "7870345240:AAE_SzWEZAwU-OzZ_J48ulm-zU8-D-ImduE"
bot = telebot.TeleBot(TOKEN)

def find_movie_by_code(code):
    try:
        with open('data.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for value in row.values():
                    if value.strip() == code.strip():
                        return row.get('nazva', 'Назва відсутня'), row.get('посилання', '#')
    except FileNotFoundError:
        print("❌ Файл data.csv не знайдено!")
    return None, None

def get_random_movie():
    try:
        with open('data.csv', 'r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file))
            random_movie = random.choice(reader)
            movie_name = random_movie.get('nazva', 'Назва відсутня')
            trailer_link = random_movie.get('посилання', '#')
            return movie_name, trailer_link
    except FileNotFoundError:
        print("❌ Файл data.csv не знайдено!")
    return "Невідомий фільм", "#"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Вітаю! Надішліть код з TikTok, щоб отримати трейлер фільму.\n\nАбо просто запитайте випадковий фільм.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_code = message.text.strip()
    movie_name, trailer_link = find_movie_by_code(user_code)

    if movie_name:
        response = f"🎬 *{movie_name}*\n🔗 [Дивитись трейлер]({trailer_link})"
    else:
        movie_name, trailer_link = get_random_movie()
        response = f"❌ Фільм за цим кодом не знайдено. Ось випадковий фільм:\n\n🎬 *{movie_name}*\n🔗 [Дивитись трейлер]({trailer_link})"

    bot.reply_to(message, response, parse_mode='Markdown', disable_web_page_preview=True)

if __name__ == '__main__':
    print("✅ Бот запущено! Перевірте Telegram.")
    bot.polling()
