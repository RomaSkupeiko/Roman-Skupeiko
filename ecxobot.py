import telebot

bot = telebot.TeleBot(token='7534768636:AAGp5qAKhqyvOgDRXotHAa_jhBYpAHjtYdA')

@bot.message_handler(content_types=['text'])
def repear_all_messages(messages):
    bot.send_message(messages.chat.id, messages.text)

bot.infinity_polling()