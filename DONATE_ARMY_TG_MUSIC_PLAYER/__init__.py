import json
import os

from DONATE_ARMY_TG_MUSIC_PLAYER.core.bot import DONATE_ARMY_BOT
from DONATE_ARMY_TG_MUSIC_PLAYER.core.dir import dirr
from DONATE_ARMY_TG_MUSIC_PLAYER.core.git import git
from DONATE_ARMY_TG_MUSIC_PLAYER.core.userbot import Userbot
from DONATE_ARMY_TG_MUSIC_PLAYER.core.youtube import DONATE_ARMY_MUSIC
from DONATE_ARMY_TG_MUSIC_PLAYER.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()

git()

dbb()

heroku()

sudo()

DONATE_ARMY_MUSIC()

app = DONATE_ARMY_BOT()

userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
