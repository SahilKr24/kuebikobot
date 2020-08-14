from telegram.ext import updater
import subprocess
import re
import aria
def button(update,context):
    query = update.callback_query
    query.answer()
    data = query.data
    if data.startswith("pause:"):
        gid = data.replace('pause:','')
        download = aria.aria2.get_download(gid)
        try:
            aria.aria2.pause([download])
            print("Download Paused(btn)")
        except Exception as e:
            print(e)     

    if data.startswith("resume:"):
        gid = data.replace('resume:','')
        download = aria.aria2.get_download(gid)
        try:
            download.update()
            download.resume()
            print("Download Resumed(btn)")
        except Exception as e:
            print(e)

    if data.startswith("cancel:"):
        gid = data.replace('cancel:','')
        download = aria.aria2.get_download(gid)
        try:
            download.update()
            download.remove(force=True,files=True)
            print("Download Cancelled(btn)")
        except Exception as e:
            print(e)

def uploader(updater,update,message,download,ftype):
    updateText = f"Download Completed \n'{download.name}'\nSize : {(float(download.total_length)/ 1024 ** 2):.2f} MBs"
    updater.bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=updateText)
    current = update.message.reply_text(f"{download.name} is complete, \nUploading now")
    if ftype == 'folder':
        op = subprocess.run(['bash','folder.sh',f"{download.name}"],check=True,stdout=subprocess.PIPE).stdout.decode('utf-8')
    if ftype == 'file':
        op = subprocess.run(['bash','commands.sh',f"downloads/{download.name}"],check=True,stdout=subprocess.PIPE).stdout.decode('utf-8')
    link = urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', op)
    print(link)
    print("Download instance finished")
    updater.bot.send_message(chat_id=-474404045,text=f'Upload complete')
    updater.bot.edit_message_text(chat_id=message.chat.id,message_id=current.message_id,text=str(link[0]))