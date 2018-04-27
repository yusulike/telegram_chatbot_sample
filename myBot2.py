from telegram.ext import Updater, CommandHandler
# 추가
from telegram.ext import MessageHandler, Filters

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

# 추가: 메시지 수신 시 처리 함수
def get_message(bot, update) :
     update.message.reply_text(
        'Say {}'.format(update.message.text))

updater = Updater('YOUR BOT TOKEN ID')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
# 추가: 메시지 핸들러 추가
updater.dispatcher.add_handler(MessageHandler(Filters.text, get_message))

updater.start_polling()
updater.idle()