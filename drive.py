from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import shutil

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("token.json")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("token.json")

drive = GoogleDrive(gauth)

if __name__=="__main__":
	textfile = drive.CreateFile()
	textfile.SetContentFile('eng.txt')
	textfile.Upload()
	print (textfile)
	drive.CreateFile({'id':textfile['id']}).GetContentFile('eng-dl.txt')

def uploadfile(filename):
    file1 = drive.CreateFile()
    shutil.move(f"{filename}",f"downloads/{filename}")
    file1.SetContentFile(filename)
    file1.Upload()
    permission = file1.InsertPermission({
        'type': 'anyone',
        'value': 'anyone',
        'role': 'reader'})
    os.remove(filename)
    return file1['alternateLink']
