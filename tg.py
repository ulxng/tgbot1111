import telebot

bot = telebot.TeleBot("7753353919:AAGEomI4uCCdRVm1dxQ0nxTpViQvLVgxWh4")


@bot.message_handler(commands=["start", "help"])
def send_message(message):
    bot.reply_to(message="Hello world!")


bot.polling(none_stop=True, interval=0)
