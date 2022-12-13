from bot.bot import Bot
from bot.handler import MessageHandler


TOKEN = "001.1233165946.2833803999:1007718755"
bott = Bot(token = TOKEN)

def msg_cb(bot, event):
    if 'ит ' in event.text:
        clear_ticket = event.text.replace('ит ', '')

        bot.send_text(chat_id=event.from_chat, text='Записал в файл для ИТ')
    elif 'другое ' in event.text:
        clear_ticket = event.text.replace('другое ', '')

        bot.send_text(chat_id=event.from_chat, text='Записал в файл Другое')

bott.dispatcher.add_handler(MessageHandler(callback=msg_cb))

bott.start_polling()
bott.idle()