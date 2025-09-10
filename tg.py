import telebot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = telebot.TeleBot(BOT_TOKEN)


phrases = {"помощь где?", "хелп ми", "мне нужна помощь", "i need help", "помощь", "хелп", "help"}


@bot.message_handler(commands=["start"])
def send_start_message(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Привет, {message.from_user.first_name} {message.from_user.last_name}",
    )
    print(f"Обработана команда /start от пользователя ID: {message.from_user.id}")


@bot.message_handler(commands=["help"])
def send_help_message(message):
    bot.reply_to(message, "Тебе тут никто не поможет.")
    print(f"Обработана команда /help от пользователя ID: {message.from_user.id}")


@bot.message_handler(commands=["me"])
def send_me_message(message):
    bot.reply_to(message, {message.from_user.id})
    print(f"Обработана команда /me от пользователя ID: {message.from_user.id}")


@bot.message_handler(func=lambda message: message.text.strip() in phrases)
def send_help1_message(message):
    check = message.text.strip()

    if check == "хелп ми":
        bot.reply_to(message, "Тебе тут никто не поможет.")
        print(f"Обработана команда /help1 от пользователя ID: {message.from_user.id}")
    elif check == "помощь где?":
        bot.reply_to(message, "Тебе тут никто не поможет.")
        print(f"Обработана команда /help1 от пользователя ID: {message.from_user.id}")
    elif check == "мне нужна помощь":
        bot.reply_to(message, "Тебе тут никто не поможет.")
        print(f"Обработана команда /help1 от пользователя ID: {message.from_user.id}")
    elif check == "I need help":
        bot.reply_to(message, "Тебе тут никто не поможет.")
        print(f"Обработана команда /help1 от пользователя ID: {message.from_user.id}")
    elif check == "help":
        bot.reply_to(message, "Тебе тут никто не поможет.")
        print(f"Обработана команда /help1 от пользователя ID: {message.from_user.id}")
    elif check == "хелп":
        bot.reply_to(message, "Тебе тут никто не поможет.")
        print(f"Обработана команда /help1 от пользователя ID: {message.from_user.id}")
    elif check == "помощь":
        bot.reply_to(message, "Тебе тут никто не поможет.")
        print(f"Обработана команда /help1 от пользователя ID: {message.from_user.id}")

def main():
    bot.polling(none_stop=True, interval=1)


if __name__ == "__main__":
    print("Бот запущен.")
    main()
