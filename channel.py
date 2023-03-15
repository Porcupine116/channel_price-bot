import telebot
import time
from telegram import ParseMode

TOKEN = '5786523725:AAGZXmZT3KpP0sPQ_suLBSqA4uBmbUCe4gM'
CHAT_ID = '-1001985839334'
LINK_BOT = 'https://t.me/ninja_cryptobot'
TEXT_BOT =  'КЛАЦ {}.'.format(LINK_BOT)
MESSAGE = 'Дорогие барыги и участники сообщества NiNJA 🥷🏿 Crypto\n\n'\
          'Мы не приемлем неуважительное  общение и агрессию между участниками!\n\n'\
          'Мы запрещаем:\n'\
          '📌 Рекламу и спам в любом их проявлении.\n'\
          '📌 Оскорбления, агрессию, провокации на политические, расовые, гендерные или другие конфликтные темы.\n\n'\
          'Мы поощряем любое ДОБРОЖЕЛАТЕЛЬНОЕ общение!\n\n'\
          '🚫 Администрация комьюнити не проводит консультаций в личных сообщениях и не обращается к подписчикам в ЛС первыми!\n\n\n'\
          '💡Наши ресурсы:\n\n'\
          '🤖 Незаменимый бот: <a href="https://t.me/ninja_cryptobot">КЛАЦ</a>\n'\
          '🥷🏿 Авторский канал: <a href="https://t.me/ninja_crypto">КЛАЦ</a>\n'\
          '🗞 Новостной канал: <a href="https://t.me/ninjacrypto_news">КЛАЦ</a>\n'\
          '🚨 Сигналы от подписчиков: <a href="https://t.me/ninjacrypto_signal">КЛАЦ</a>\n'\
          '📚 Бесплатное обучение: <a href="https://telegra.ph/Navigaciya-07-18-2">КЛАЦ</a>\n'\
          '📕Курс по Smart-Money: <a href="https://telegra.ph/Navigaciya-Smart-Mani-01-19">КЛАЦ</a>\n'\
          '💰 Стратегии торговли: <a href="https://telegra.ph/Strategii-torgovli-01-19">КЛАЦ</a>\n'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_message(message):
    while True:
        try:
            bot.delete_message(CHAT_ID, message_id=message.id)
        except:
            pass
        #bot.send_message(CHAT_ID, MESSAGE)
        bot.send_message(chat_id=CHAT_ID, text=MESSAGE, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        time.sleep(10) # 8 hours

bot.polling()