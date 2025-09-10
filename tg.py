import telebot 
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") 


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_start_message(message):
    bot.reply_to(message, f"Привет, {message.from_user.first_name} {message.from_user.last_name}")
    print(f"Обработана команда /start от пользователя ID: {message.from_user.id}")


@bot.message_handler(commands=["help"])
def send_help_message(message):
    bot.reply_to(message, "Тебе тут никто не поможет.")
    print(f"Обработана команда /help от пользователя ID: {message.from_user.id}")


@bot.message_handler(commands=["me"])
def send_me_message(message):
    bot.reply_to(message, {message.from_user.id})
    print(f"Обработана команда /me от пользователя ID: {message.from_user.id}")


@bot.message_handler(content_types=['text'])
def send_help1_message(message):
    if message.text.upper() == 'help' or 'помощь' or 'хелп':
        bot.reply_to(message, "Тебе тут никто не поможет.")
        print(f"Обработана команда /help1 от пользователя ID: {message.from_user.id}")
    

def main():
    bot.polling(none_stop=True, interval=1)


print("Бот запущен.")


if __name__ == "__main__":
    main()



