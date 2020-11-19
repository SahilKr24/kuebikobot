import aria2p
import socket
import os

from aria2p.downloads import Download
host = socket.gethostbyname('aria2-pro')


# Instance of Aria2 api
# This line connects the bot to the aria2 rpc server

aria2:aria2p.API = aria2p.API(
    aria2p.Client(
        host=f"http://{host}",
        secret=os.environ.get("RPC_SECRET")
    )
)


def addDownload(link: str) -> None:
    """Adds download link to aria and starts the download

    Args:
        link: Download url link
    """
    link = link.replace('/mirror', '')
    link = link.strip()
    download:Download = aria2.add_magnet(link)
    while download.is_active:
        print("downloading")
    if(download.is_complete):
        print("Download complete")


downloads = aria2.get_downloads()
