import telebot

bot = telebot.TeleBot("7753353919:AAGEomI4uCCdRVm1dxQ0nxTpViQvLVgxWh4")


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text.upper() == "1":
        bot.send_message(message.from_user.id, "2")
    else:
        pass


bot.polling(none_stop=True, interval=0)
