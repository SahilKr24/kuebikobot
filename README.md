<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="Bot logo"></a>
</p>

<h3 align="center">kuebiko bot</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Platform](https://img.shields.io/badge/platform-heroku-lightgrey)]()
[![GitHub Issues](https://img.shields.io/github/issues/sahilkr24/kuebikobot)](https://github.com/SahilKr24/kuebikobot/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/SahilKr24/kuebikobot)](https://github.com/SahilKr24/kuebikobot/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 A telegram bot that deploys to heroku and downloads links and torrents and uploads to google drive and returns public share link. 
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Demo / Working](#demo)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [Deploying your own bot](#deployment)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This bot is written in python and imports aria2 for downloading files and magnet links and uploads to google drive via drive-cli then returns direct download/share link with visibility set to public for easy sharing.

This bot is asynchronous and also has pause and cancel buttons of easy management of downloads.

## 🎥 Demo / Working <a name = "demo"></a>

![Working](https://media.giphy.com/media/20NLMBm0BkUOwNljwv/giphy.gif)

Will be updated shortly!

## 💭 How it works <a name = "working"></a>

The bot first extracts the link from the the command it's called from and then adds it to aria2 cli via webhooks, after that it will show progress every 2 seconds in form of message updates.

Once the download completes it will then proceed to upload the file/folder using predefined scripts that will then return the shared link in form of a reply to the original message.

The entire bot is written in Python 3.7

## 🎈 Usage <a name = "usage"></a>

To use the bot, type:

```
/help
```
or

```
/start (personal message only)
```

All commands, i.e. "/help" **are not** case sensitive.

The bot will then give you the help context menu.

### Start:

> /help
**Response:**

**/mirror**  :for http(s),ftp and file downloads

**/magnet**  :for torrent magnet links

**/cancel**  :cancel all in progress downloads

**/list**    :get a list of downloads

use these commands along with your link or magnets.

### Example:

```
/mirror https://releases.ubuntu.com/20.04/ubuntu-20.04.1-desktop-amd64.iso
```
**Response:**

>Mirror, [14.08.20 19:57]<br>
>[In reply to Sahil]<br>
>Downloading <br>
>'ubuntu-20.04.1-desktop-amd64.iso'<br>
>Progress : 17.62/2656.00 MBs <br>
>at 33.53 MBps<br>
>[--------------------] 0.7 %<br>


>Mirror, [14.08.20 19:59]<br>
>[In reply to Sahil]<br>
>https://drive.google.com/open?id=<- id of the file -><br>

>Mirror, [14.08.20 19:59]<br>
>Upload complete<br>
---
<sup>Beep boop. I am a bot. If there are any issues, contact at my [GitHub](https://github.com/SahilKr24/kuebikobot)</sup>

<sup>Want to make a similar bot? Check out: [GitHub](https://github.com/SahilKr24/kuebikobot)</sup>

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on heroku.

### Prerequisites

All the prerequisites are mentioned in the requirements.txt. Additionally, you'll need to install aria2c on your linux machine if you want to run a local version.
You'll also need to get google credentials for the google drive via API dashboard from google developers console.

```
aria2c
credentials.json
bot id from bot father (telegram)
```

### Installing

First, copy the credentials.json in the root directory and update the bot id in bot.py at line 14.

Switch to venv and install all the requirements from requirements.txt

```
run python3 bot.py
```

When you run for the first time, it will ask you to authorise or refresh token for drive using local web server, follow the link from terminal and open in any web browser. After authenticating copy back the access code to cli. This will create token.json which is importantand should be kept securely.

That's it.
The bot should send a **bot started** message on the channels it addded to verifying it's active.

You're bot is now ready to use. Yay!

## 🚀 Deploying your own bot <a name = "deployment"></a>

To deploy your bot on heroku, please follow the above steps and then procced below:
Procfile and and other settings have already been added as per needs.

- **Heroku**: https://github.com/SahilKr24/kuebikobot

>Push the repo to your local github and set up a deployment in heroku.
Add the following buildpacks under **Settings > Buildpacks**
>heroku/python<br>
>https://github.com/amivin/aria2-heroku.git
the second buildpack will ensure that aria is installed on the dyno on which the bot will run.

After that deploy your branch and if everything is correctly configured, the bot will reply with **bot started** message in the channels.

## ⛏️ Built Using <a name = "built_using"></a>

- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/) - This library provides a pure Python interface for the Telegram Bot API.
- [Heroku](https://www.heroku.com/) - SaaS hosting platform
- [aria2p](https://pypi.org/project/aria2p/) - Command-line tool and library to interact with an aria2c daemon process with JSON-RPC.
- [aria2c](https://github.com/aria2/aria2) - aria2 is a lightweight multi-protocol & multi-source, cross platform download utility operated in command-line. 
- [pydrive](https://pypi.org/project/PyDrive/) - Google Drive API made easy.


## ✍️ Authors <a name = "authors"></a>

- [@Rkrohk](https://github.com/Rkrohk) - Inital Idea & Scripting
- [@SahilKr24](https://github.com/SahilKr24) - Scripting & Dev-Ops

See also the list of [contributors](https://github.com/SahilKr24/kuebikobot/contributors) who participated in this project.
