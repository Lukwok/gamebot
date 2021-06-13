import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', 5000))    

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1601794899:AAFYCbypGF4UT-LW5WPlIXSmLodW2257vQI'

#variable list
avaList = []

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    output = """特別嗚謝可愛嘅路過!! >W< \n全體成員, 家族戰報名表 (六/日20:00-21:00) Version 1.4"""
    groupid = update.message.chat.id

    #only Auto and admin group can empty list
    if (groupid == "-515223688" or groupid =="816970229"):
        global avaList
        avaList = []
    update.message.reply_text(output)

def help(update, context):
    """Send a message when the command /help is issued."""
    output = """皆さん~ 路過sansan 教你點用 <3 \n
注意!! 此乃路過一日亂整出黎! 請不要同人分享或自己亂玩\n
所有資料被第三方改動,路過不會負責~~ (我懶)\n
1. /start \t 唔好亂用 !!佢會restart個bot同清空record!!\n
2. /join [name] \t 如果得閒打族戰就報名la\n
4. /delete [name] \t 哎? ざんねん~ 原來我都係唔得閒打.. \n
6. /show \t 出List\n
7. /close \t 898 \n
8. /help \t 召喚我 \n\n
仲有冇咩唔明? 但就算有我都幫你唔到 :P """
    update.message.reply_text(output)

def join(update, context):
    try:
        input = update.message.text[6:]
        if input:
            global avaList
            item = {"updater":update.message.from_user.full_name,"gameName":input,"id":update.message.from_user.id}
            avaList.append(item)
            output = """Input Successful"""
            update.message.reply_text(output)
        else:
            raise Exception()
    except:
        output = """Error"""
        update.message.reply_text(output) 

def show(update, context):
    output = """全體成員，今個星期六/日20:00-21:00家族戰，會出戰請在下方留名，要預先安排崗位

    !!參加者必須參與兩場團體戰一場個人戰!! 

    ⚠ :無指定時間會視為隨時侯命 ⚠ \n\n"""
    counter = 1
    global avaList
    for i in avaList:
         input = "{0}. {1} {2} \n".format(counter, i["updater"], i["gameName"])
         output = output+input
         counter +=1

    update.message.reply_text(output) 

def delete(update,context):
    input = update.message.text[8:]
    try:
        if input:
            id = update.message.from_user.id
            counter =  0
            global avaList
            for i in avaList:
                if (i["id"]==id and i["gameName"]==input):
                    avaList.pop(counter)
                    output = """Delete Sucessfully"""
                    update.message.reply_text(output)
                    break
                counter +=1
        else: raise Exception()
    except:
        output = """Error"""
        update.message.reply_text(output)

def close(update,context):
    update.message.reply_text("Sor9, 未得閒做住~~")




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
    dp.add_handler(CommandHandler("show", show))
    dp.add_handler(CommandHandler("delete", delete))
    dp.add_handler(CommandHandler("close", close))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    #dp.add_error_handler(error)

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
