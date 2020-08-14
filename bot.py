# -*- coding: utf-8 -*-
import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher, CallbackQueryHandler
from telegram.ext.dispatcher import run_async
import aria
import time
from services import murror, muggnet
from handlers import button

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

updater = Updater("< bot id >", use_context=True)

def id(update,context):
    chatid = update.message.chat.id
    update.message.reply_text(chatid)
    updater.bot.send_message(chat_id=chatid, text="Here is the id")

def cri(update,context):
    chatid = update.message.chat.id
    criemoji = u'\U0001F62D'
    f = open('sticker/criduck.tgs', 'rb')
    update.message.reply_text(criemoji + criemoji + criemoji)
    updater.bot.send_sticker(chat_id=chatid,sticker=f)

def start(update,context):
    update.message.reply_text(f"Hello " + update.message.chat.first_name +"\nFor help send /help")

def help_func(update,context):
    update.message.reply_text(f"/mirror    :for http(s),ftp and file downloads\n/magnet :for torrent magnet links\n/cancel    :cancel all in progress downloads\n/list          :get a list of downloads")

def listdownloads(update,context):
    listofdownloads=[]
    downloads = aria.aria2.get_downloads()
    for dwld in downloads:
        listofdownloads.append(dwld.name)
    update.message.reply_text(listofdownloads)

def cancel(update,context):
    downloads = aria.aria2.get_downloads()
    try:
        aria.aria2.remove(downloads=downloads,files=True,clean=True,force=True)
    except:
        print("No downloads to delete")
    update.message.reply_text("Cancelling all downloads")

def error(update, context):
    """Log Errors caused by Updates."""
    updater.bot.send_message(chat_id=-474404045,text=f'Update {update} caused error {context.error}')
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def custom_error(custom_message):
    updater.bot.send_message(chat_id=-474404045,text=custom_message)

@run_async
def mirror(update, context):
    try:
        murror(update=update,updater=updater,context=context)
    except:
        custom_error("Mirror function returned an error")
    
@run_async
def magnet(update, context):
    try:
        muggnet(update=update,updater=updater,context=context)
    except:
        custom_error("Magnet function returned an error")

def main():
    updater.bot.send_message(chat_id=-474404045,text="Bot Started")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help_func))
    dp.add_handler(CommandHandler('mirror',mirror))
    dp.add_handler(CommandHandler('magnet',magnet))
    dp.add_error_handler(error)
    dp.add_handler(CommandHandler("list",listdownloads))
    dp.add_handler(CommandHandler("id",id))
    dp.add_handler(CommandHandler("cri",cri))
    dp.add_handler(CommandHandler("cancel",cancel))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
