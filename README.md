# DONATE_ARMY_TG_MUSIC_PLAYER BOT

A powerful Telegram music bot for voice chats with features like YouTube, Spotify, Resso, AppleMusic, and Soundcloud support.

## 🎯 Features

- YouTube, Spotify, Resso, AppleMusic & Soundcloud support 
- Written in Python with Pyrogram and Py-Tgcalls
- Heroku and VPS deployment support
- Channel and group voice chat playback
- Inline search support
- YouTube thumbnail search
- Unlimited queue
- Broadcast messages
- Detailed stats and user analytics
- Block/Unblock user management
- Multi-language support
- Playlist management

## ⚡️ Quick Setup

### Heroku Deployment 
[![Deploy on Heroku](https://img.shields.io/badge/Deploy%20On%20Heroku-purple?style=for-the-badge&logo=heroku)](https://dashboard.heroku.com/new?template=https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER)

### 🖇 VPS Deployment
- Clone repo: `git clone https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER && cd DONATE_ARMY_TG_MUSIC_PLAYER`
- Setup by: `bash setup`
- Fill [Extra Variables](https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER/blob/master/sample.env) by `nano .env`, save changes with `CTRL+X`, then `y`, then `Enter`
- Install tmux: `sudo apt install tmux && tmux`
- Run the bot: `bash start`
- To exit tmux session: Press `Ctrl+b` and then `d`

### ⚙️ Config Variables
Required variables:
- `API_ID` - Get from my.telegram.org
- `API_HASH` - Get from my.telegram.org
- `BOT_TOKEN` - Get from @BotFather
- `MONGO_DB_URI` - MongoDB database URL
- `LOG_GROUP_ID` - Group ID for logging
- `OWNER_ID` - Your Telegram user ID
- `STRING_SESSION` - Pyrogram string session (Pyrogram v2)
- 
Optional variables:
- `SPOTIFY_CLIENT_ID` - Spotify client ID
- `SPOTIFY_CLIENT_SECRET` - Spotify client secret
- `HEROKU_API_KEY` - Heroku API key
- `HEROKU_APP_NAME` - Heroku app name
See [**config docs**](https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER/blob/master/config%2FREADME.md) for full list of variables

### 🤝 Support
- Join [**DONATE_ARMY_BOTS ™**](https://t.me/DONATE_ARMY_BOTS) for updates
- Join [**OUR SUPPORT GROUP**](https://t.me/DONATE_ARMY_BOTS_SUPPORT_CHAT) for support

### 📃 License
This project is licensed under the [**MIT License**](https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER/blob/master/LICENSE)

### 🙋‍♂️ Credits
- [**𝘿𝙊𝙉𝘼𝙏𝙀 ๛ 𝘼𝙍𝙈𝙔 🇮🇳 ™**](https://t.me/+TEOLVuOuPl01Y2U1)

### 🙏 Special Thanks

A heartfelt thanks to [**Team Yukki**](https://github.com/TeamYukki) for creating the amazing  [**YukkiMusicBot**](https://github.com/TeamYukki/YukkiMusicBot) that inspired this project!
