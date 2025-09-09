import telebot


BOT_TOKEN = "7966123957:AAHd89O9laVRJ8HCQ9sKSnoBF-FqiRYYuOQ"


bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=["start"])
def send_start_message(message):
    bot.reply_to(message, "Hello world!")
    print(f"Обработана команда /start от пользователя ID: {message.from_user.id}")

@bot.message_handler(commands=["help"])
def send_help_message(message):
    bot.reply_to(message, "Тебе тут никто не поможет.")
    print(f"Обработана команда /help от пользователя ID: {message.from_user.id}")

@bot.message_handler(commands=["me"])
def send_me_message(message):
    bot.reply_to(message, {message.from_user.id})
    print(f"Обработана команда /me от пользователя ID: {message.from_user.id}")

print("Бот запущен.")

def main():
    bot.polling(none_stop=True, interval=1)
if __name__ == "__main__": 
    main()
