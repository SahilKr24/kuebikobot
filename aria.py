import aria2p
import socket
import os
host = socket.gethostbyname('aria2-pro')

aria2 = aria2p.API(
    aria2p.Client(
        host=f"http://{host}",
        secret=os.environ.get("RPC_SECRET")
    )
)

def addDownload(link):
    link = link.replace('/mirror','')
    link = link.strip()
    print(link)
    download = aria2.add_magnet(link)
    while download.is_active:
        print("downloading")
    if(download.is_complete):
        print("Download complete")

downloads = aria2.get_downloads()

def main():
    for download in downloads:
        print(download.name, download.download_speed)

if __name__ == "__main__":
    main()
