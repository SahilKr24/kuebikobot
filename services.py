import aria
import time
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from handlers import uploader

def build_menu(buttons,
               n_cols):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    return menu

def create_markup(gid):
    button_list = [
        InlineKeyboardButton("pause",callback_data=f"pause:{gid}"),
        InlineKeyboardButton("cancel",callback_data=f"cancel:{gid}")
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(buttons=button_list,n_cols=2))
    return reply_markup

def create_resume_button(gid):
    button_list = [
        InlineKeyboardButton("resume",callback_data=f"resume:{gid}"),
        InlineKeyboardButton("cancel",callback_data=f"cancel:{gid}")
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(buttons=button_list,n_cols=2))
    return reply_markup

def progessbar(new,tot):
    length = 20
    progress = int(round(length * new /float(tot)))
    percent = round(new/float(tot) * 100.0,1)
    bar = '=' * progress + '-' * (length - progress)
    return '[%s] %s %s\r' % (bar,percent,'%')

@run_async
def murror(update,updater,context):
    link = update.message.text
    message = update.message.reply_text("Starting...")
    link = link.replace('/mirror','')
    link = link.strip()
    print(link)
    try:
        download = aria.aria2.add_uris([link])
    except Exception as e:
        print(e)
        if (str(e).endswith("No URI to download.")):
            updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="No link provided!")
            return None
            
    prevmessage = None
    time.sleep(1)
    while download.is_active or not download.is_complete:

        try:
            download.update()
        except Exception as e:
                if (str(e).endswith("is not found")):
                    print("Mirror Deleted")
                    updater.bot.edit_mtessage_text(chat_id=message.chat.id,message_id=message.message_id,text="Download removed")
                    break
                print(e)
                print("Issue in downloading!")

        if download.status == 'removed':
            print("Mirror was cancelled")
            updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="Download removed")
            break

        if download.status == 'error':
            print("Mirror had an error")
            download.remove(force=True,files=True)
            updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="Download failed to resume/download!")
            break

        print(f"Mirror Status? {download.status}")

        if download.status == "active":
            try:
                download.update()
                barop = progessbar(download.completed_length,download.total_length)
                print(barop)
                updateText = f"Downloading \n'{download.name}'\nProgress : {(float(download.completed_length)/ 1024 ** 2):.2f}/{(float(download.total_length)/ 1024 ** 2):.2f} MBs \nat {(float(download.download_speed)/ 1024 ** 2):.2f} MBps\n{barop}"
                if prevmessage != updateText:
                    updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=updateText,reply_markup=create_markup(download.gid))
                    prevmessage = updateText
                print("downloading")
                time.sleep(2)
            except Exception as e:
                if (str(e).endswith("is not found")):
                    break
                print(e)
                print("Issue in downloading!/Flood Control")
                time.sleep(2)
        elif download.status == "paused":
            try:
                download.update()
                updateText = f"Download Paused \n'{download.name}'\nProgress : {(float(download.completed_length)/ 1024 ** 2):.2f}/{(float(download.total_length)/ 1024 ** 2):.2f} MBs"
                if prevmessage != updateText:
                    updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=updateText,reply_markup=create_resume_button(download.gid))
                    prevmessage = updateText
                print("paused")
                time.sleep(2)
            except Exception as e:
                print(e)
                print("Download Paused Flood!")
                time.sleep(2)
        time.sleep(2)

    if download.status == "complete":
        if download.is_complete:
            print(download.name)
            try:
                uploader(updater,update,message,download,'folder')
            except Exception as e:
                    print(e)
                    print("Upload Issue!")
    return None

@run_async
def muggnet(update,updater,context):
    link = update.message.text
    message = update.message.reply_text("Starting...")
    link = link.replace('/magnet','')
    link = link.strip()

    try:
        download = aria.aria2.add_magnet(link)
    except Exception as e:
        print(e)
        if (str(e).endswith("No URI to download.")):
            updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="No link provided!")
            return None

    prevmessagemag = None

    while download.is_active:
        try:
            download.update()
            print("Downloading metadata")
            updateText = f"Downloading \n'{download.name}'\nProgress : {(float(download.completed_length)/ 1024):.2f}/{(float(download.total_length)/ 1024):.2f} KBs"
            if prevmessagemag != updateText:
                updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=updateText)
                prevmessagemag = updateText
            time.sleep(2)
        except:
            print("Metadata download problem/Flood Control Measures!")
            try:
                download.update()
            except Exception as e:
                if (str(e).endswith("is not found")):
                    print("Metadata Cancelled/Failed")
                    updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="Metadata couldn't be downloaded")
                    return None
            time.sleep(2)

    time.sleep(2)
    match = str(download.followed_by_ids[0])
    downloads = aria.aria2.get_downloads()
    currdownload = None
    for download in downloads:
        if download.gid == match:
            currdownload = download
            break
    print("Download complete")
    prevmessage = None
    while currdownload.is_active or not currdownload.is_complete:

        try:
            currdownload.update()
        except Exception as e:
            if (str(e).endswith("is not found")):
                print("Magnet Deleted")
                updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="Magnet download was removed")
                break
            print(e)
            print("Issue in downloading!")

        if currdownload.status == 'removed':
            print("Magnet was cancelled")
            updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="Magnet download was cancelled")
            break

        if currdownload.status == 'error':
            print("Mirror had an error")
            currdownload.remove(force=True,files=True)
            updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="Magnet failed to resume/download!\nRun /cancel once and try again.")
            break

        print(f"Magnet Status? {currdownload.status}")

        if currdownload.status == "active":
            try:
                currdownload.update()
                barop = progessbar(currdownload.completed_length,currdownload.total_length)
                print(barop)
                updateText = f"Downloading \n'{currdownload.name}'\nProgress : {(float(currdownload.completed_length)/ 1024 ** 2):.2f}/{(float(currdownload.total_length)/ 1024 ** 2):.2f} MBs \nat {(float(currdownload.download_speed)/ 1024 ** 2):.2f} MBps\n{barop}"
                if prevmessage != updateText:
                    updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=updateText,reply_markup=create_markup(currdownload.gid))
                    prevmessage = updateText
                time.sleep(2)
            except Exception as e:
                if (str(e).endswith("is not found")):
                    break
                print(e)
                print("Issue in downloading!")
                time.sleep(2)
        elif currdownload.status == "paused":
            try:
                currdownload.update()
                updateText = f"Download Paused \n'{currdownload.name}'\nProgress : {(float(currdownload.completed_length)/ 1024 ** 2):.2f}/{(float(currdownload.total_length)/ 1024 ** 2):.2f} MBs"
                if prevmessage != updateText:
                    updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=updateText,reply_markup=create_resume_button(currdownload.gid))
                    prevmessage = updateText
                time.sleep(2)
            except Exception as e:
                print(e)
                print("Download Paused Flood")
                time.sleep(2)
        time.sleep(2)

    time.sleep(1)
    if currdownload.is_complete:
        print(currdownload.name)
        try:
            uploader(updater,update,message,currdownload,'folder')
        except Exception as e:
                print(e)
                print("Upload Issue!")
    return None