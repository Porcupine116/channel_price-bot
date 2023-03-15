import json
import time
from telegram.ext import CommandHandler, Updater, MessageHandler, PrefixHandler
import requests
import telegram

# Здесь нужно указать токен вашего бота
TOKEN = '5786523725:AAGZXmZT3KpP0sPQ_suLBSqA4uBmbUCe4gM'


# Здесь нужно указать ваш API-ключ и секретный ключ Binance
API_KEY = 'cpHUx4GbhWkgnQM5Z94Z324aDUmXdkg9DJDSxRDeWOmh27pmzozkZA3rQomXuUNE'
SECRET_KEY = 'Pi9SV1h2FJyv5geB6iHzlJOKu2g0Lvj9F24dFc0qs0i8A0mbK30MgeCzSmi6xcJy'
# Создаем объекты для работы с Telegram и Binance API
bot = telegram.Bot(token=TOKEN)
binance_api_url = 'https://fapi.binance.com'


# Функция для получения цены и изменения цены за определенный период
def get_price_and_change(symbol, interval):
  # Получаем данные о свечах за нужный период
  candles_url = f'{binance_api_url}/fapi/v1/klines?symbol={symbol}&interval={interval}'
  candles_response = requests.get(candles_url)
  candles_data = json.loads(candles_response.text)

  # Получаем цену закрытия последней свечи и цену закрытия свечи, которая была interval назад
  last_candle_close_price = float(candles_data[-1][4])
  prev_candle_close_price = float(candles_data[-2][4])

  # Вычисляем изменение цены за нужный период
  price_change = round((last_candle_close_price - prev_candle_close_price) / prev_candle_close_price * 100, 2)

  # Получаем текущую цену
  price_url = f'{binance_api_url}/fapi/v1/ticker/price?symbol={symbol}'
  price_response = requests.get(price_url)
  price_data = json.loads(price_response.text)
  current_price = float(price_data['price'])

  # Возвращаем результат
  return current_price, price_change


# Функция-обработчик команды /price
def price_handler(update, context):
  # Получаем символ криптовалюты из аргументов команды
  symbol = context.args[0].upper()

  # Получаем цену и изменение цены за 15 минут, 1 час и 1 день
  price_15m, change_15m = get_price_and_change(f'{symbol}USDT', '15m')
  price_1h, change_1h = get_price_and_change(f'{symbol}USDT', '1h')
  price_1d, change_1d = get_price_and_change(f'{symbol}USDT', '1d')

  # Отправляем сообщение с результатом
  message = f'Цена {symbol}: {price_15m:.2f} USDT\n\n'
  message += f'Изменение цены:\n'
  message += f'за 15 минут: {change_15m}%\n'
  message += f'За 1 час: {change_1h}%\n'
  message += f'За 1 день: {change_1d}%'
  # Удаляем сообщение через 1 минуту
  if '!p' in update.message.text:
    message1 = update.message.reply_text(message)
    #context.job_queue.run_once(delete_message, 60, context=[message1.chat_id, message1.message_id])


#def delete_message(context):
#  chat_id, message_id = context.job.context
#  context.bot.delete_message(chat_id=chat_id, message_id=message_id)


def main():
  updater = Updater(TOKEN, use_context=True)
  dp = updater.dispatcher

  prefix_handler = PrefixHandler("!", "p", price_handler)

  dp.add_handler(prefix_handler)
  updater.start_polling()
  updater.idle()


main()

