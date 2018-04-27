from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import restapi_test
import json


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def get_message(bot, update) :
    print ("incoming message : %s" % (update.message.text))

    if "날씨" in update.message.text:
        response, content = restapi_test.get_weather_info("seoul,kr")
        content = json.loads(content)
        update.message.reply_text(
            '지금 날씨는 {} 입니다.'.format(
                content['query']['results']['channel']['item']['condition']['text']))
    elif "코인" in update.message.text:
        response, content = restapi_test.get_cryto_currency_info('BTC')
        content = json.loads(content)
        update.message.reply_text(
            '지금 비트코인 가격은 {} 원입니다.'.format(content['data']['closing_price']))
    else:
        update.message.reply_text(
            'Say {}'.format(update.message.text))

updater = Updater('YOUR BOT TOKEN ID')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, get_message))

updater.start_polling()
updater.idle()