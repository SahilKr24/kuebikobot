# -*- coding: utf-8 -*-
import logging
import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher, CallbackQueryHandler
from telegram.ext.dispatcher import run_async
import aria
import time
from services import murror, muggnet
from handlers import button
import handlers

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

updater = Updater(os.environ.get("BOT_API_KEY"), use_context=True)

BOT_LOG_CHAT = os.environ.get("BOT_LOG_CHAT")


def id(update: telegram.Update, context):
    """Sends a message containing the Chat Id for the current chat

    Args:
        update:
            A telegram incoming update

    """

    chatid = update.message.chat.id
    update.message.reply_text(chatid)
    updater.bot.send_message(chat_id=chatid, text="Here is the id")


def cri(update: telegram.Update, context):
    """Sends a message containing an emoji of a duck crying

    Args:
        update:
            Telegram incoming update

    """

    chatid = update.message.chat.id
    criemoji = u'\U0001F62D'
    f = open('sticker/criduck.tgs', 'rb')
    update.message.reply_text(criemoji + criemoji + criemoji)
    updater.bot.send_sticker(chat_id=chatid, sticker=f)


def start(update: telegram.Update, context):
    """Sends a hello message with help commands

    Args:
        update:
            Telegram incoming update
    """

    update.message.reply_text(
        f"Hello " + update.message.chat.first_name + "\nFor help send /help")


def help_func(update: telegram.Update, context):
    """Sends response for the "/help" command

    Args:
        update:
            Telegram incoming update
    """

    update.message.reply_text(
        f"/mirror    :for http(s),ftp and file downloads\n/magnet :for torrent magnet links\n/cancel    :cancel all in progress downloads\n/list          :get a list of downloads")


def listdownloads(update: telegram.Update, context):
    """Fetches downloads from the aria server

    Args:
        update:
            Telegram incoming update

    Returns:
        A list of downloads from the aria server

    """

    listofdownloads = [dwld for dwld in aria.aria2.get_downloads()]
    update.message.reply_text(listofdownloads)


def cancel(update: telegram.Update, context):
    """Cancels all active downloads and removes the files from the server

    Args:
        update:
            Telegram incoming update
    """

    downloads = aria.aria2.get_downloads()

    try:
        aria.aria2.remove(downloads=downloads, files=True,
                          clean=True, force=True)
    except:
        print("No downloads to delete")
    update.message.reply_text("Cancelling all downloads")


def error(update, context):
    """Log Errors caused by Updates."""
    updater.bot.send_message(
        chat_id=BOT_LOG_CHAT, text=f'Update {update} caused error {context.error}')
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def custom_error(custom_message: str):
    """Sends an error message to the BOT_LOG_CHAT group

    Args:
        custom_message:
            The custom error message to be sent to the bot log chat
    """
    updater.bot.send_message(chat_id=BOT_LOG_CHAT, text=custom_message)


@run_async
def mirror(update: telegram.Update, context):
    """Asynchronously starts a download and handles the "/mirror" command

    Args:
        update:
            Telegram incoming update
    """

    try:
        murror(update=update, updater=updater, context=context)
    except:
        custom_error("Mirror function returned an error")


@run_async
def magnet(update, context):
    """Asynchronously starts a magnet download and handles "/magnet" command

    Args:
        update:
            Telegram incoming update
    """
    try:
        muggnet(update=update, updater=updater, context=context)
    except:
        custom_error("Magnet function returned an error")


def restart(update: telegram.Update, context):
    """Restarts the bot

    Args:
        update:
            Telegram incoming update
    """
    try:
        handlers.restart(updater, update, context)
    except:
        custom_error("Nahi maanna? Mat maan!")


def resturt(update: telegram.Update, context):
    """Pulls an update from github and restarts the bot

    Args:
        update:
            Telegram incoming update
    """
    try:
        handlers.update_and_restart(updater, update, context)
    except:
        custom_error(
            "Well, I guess I didn't get an update after all\nYou can feel good about yourself now")


def echo(update: telegram.Update, context):
    """Replies to a message with the message text. Basically serves as an echo command

    Args:
        update:
            Telegram incoming update
    """
    try:
        update.message.reply_text(f"{update.message.text}")
    except:
        print("ERROR")


def main():
    updater.bot.send_message(chat_id=BOT_LOG_CHAT, text="Bot Started")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    # handles "/help" command
    dp.add_handler(CommandHandler("help", help_func))
    # handles "/mirror <url>" command
    dp.add_handler(CommandHandler('mirror', mirror))
    # handles "/magnet <magnet link>" command
    dp.add_handler(CommandHandler('magnet', magnet))

    # custom error handler to send error messages to bot log chat instead of console
    dp.add_error_handler(error)

    # handles "/list" command
    dp.add_handler(CommandHandler("list", listdownloads))

    dp.add_handler(CommandHandler("id", id))  # handles "/id" command
    dp.add_handler(CommandHandler("cri", cri))  # handles "/cri" command

    # handles "/cancel" command. Cancels all active downloads.
    dp.add_handler(CommandHandler("cancel", cancel))

    # handles button "cancel" and "pause" options
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler("restart", restart))

    # git pulls and then restarts the bot
    dp.add_handler(CommandHandler("resturt", resturt))
    dp.add_handler(CommandHandler("echo", echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
