import aria2p
import subprocess

op = subprocess.run(['bash','start.sh'],check=True,stdout=subprocess.PIPE).stdout.decode('utf-8')

aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        secret="12345678"
    )
)
