from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

print ("Start up my bot...")
# 텔레그램 플랫폼에 Updater를 등록 with token
updater = Updater('YOUR BOT TOKEN ID')
# /hello Command를 처리하는 Handler를 등록
updater.dispatcher.add_handler(CommandHandler('hello', hello))
# 봇 구동
updater.start_polling()
updater.idle()