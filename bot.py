import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', 5000))    

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1601794899:AAFYCbypGF4UT-LW5WPlIXSmLodW2257vQI'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    output = """皆さん~ 路過sansan 教你點用 <3 \n
    注意!! 此乃路過一日亂整出黎! 請不要同人分享或自己亂玩\n
    所有資料被第三方改動,路過不會負責~~ (我懶)\n
    1. /start \t 唔好亂用 !!佢會restart個bot同清空record!!\n
    2. /join [name] \t 如果得閒打族戰就報名la\n
    3. /sorry [name] \t Sor9ly, 是日要陪女陪腦細,打唔到 QWQ\n
    4. /delete [name] \t 哎? ざんねん~ 原來我都係唔得閒打.. \n
    5. /fuck [name] \t 頂,終於做完野~~可以打得~~\n
    6. /show \t 出結果\n
    7. /close \t 898 \n
    8. /help \t 召喚我 \n\n
    仲有冇咩唔明? 但就算有我都幫你唔到 :P """
    update.message.reply_text(output)

def join(bot,update):
    id = update.message.chat.id
    output = "halo"+update.message.from_user.full_name+", your id is"+id
    bot.send_message(id,output)

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("join", join))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://holanlovehk-tgbot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
