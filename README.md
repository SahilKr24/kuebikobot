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
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This bot is written in python and imports aria2 for downloading files and magnet links and uploads to google drive via drive-cli then returns direct download/share link with visibility set to public for easy sharing.

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

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🚀 Deploying your own bot <a name = "deployment"></a>

To see an example project on how to deploy your bot, please see my own configuration:

- **Heroku**: https://github.com/kylelobo/Reddit-Bot#deploying_the_bot

## ⛏️ Built Using <a name = "built_using"></a>

- [PRAW](https://praw.readthedocs.io/en/latest/) - Python Reddit API Wrapper
- [Heroku](https://www.heroku.com/) - SaaS hosting platform

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/SahilKr24/kuebikobot/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
