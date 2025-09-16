import telebot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = telebot.TeleBot(BOT_TOKEN)


def log_command(command_name, user_id):
    print(f"Обработана команда {command_name} от пользователя {user_id}")


@bot.message_handler(commands=["start"])
def send_start_message(message):
    if message.from_user.last_name:
        user_name = f"{message.from_user.first_name} {message.from_user.last_name}"
    else:
        user_name = f"{message.from_user.first_name}"
    bot.send_message(chat_id=message.chat.id, text=f"Привет, {user_name}")
    log_command("start", message.from_user.id)


@bot.message_handler(commands=["help"])
def send_help_message(message):
    bot.reply_to(message, "Тебе тут никто не поможет.")
    log_command("help", message.from_user.id)


@bot.message_handler(commands=["me"])
def send_me_message(message):
    bot.reply_to(message, {message.from_user.id})
    log_command("me", message.from_user.id)


@bot.message_handler(content_types="text")
def send_ban_message(message):
    if message.text.strip().lower().find("заработок") != -1:
        bot.reply_to(message, "Этобан")


def main():
    bot.polling(none_stop=True, interval=1)


if __name__ == "__main__":
    print("Бот запущен.")
    main()
