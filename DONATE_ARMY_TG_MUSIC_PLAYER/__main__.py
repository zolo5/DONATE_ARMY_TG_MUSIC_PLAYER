#
# Copyright (C) 2024 by DONATE_ARMY™@Github, < https://github.com/DONATE-ARMY-BOTS >.
#
# This file is part of < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER > project,
# and is released under the MIT License.
# Please see < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER/blob/master/LICENSE >
#
# All rights reserved.
import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS
from DONATE_ARMY_TG_MUSIC_PLAYER import HELPABLE, LOGGER, app, userbot
from DONATE_ARMY_TG_MUSIC_PLAYER.core.call import DONATE_ARMY
from DONATE_ARMY_TG_MUSIC_PLAYER.plugins import ALL_MODULES
from DONATE_ARMY_TG_MUSIC_PLAYER.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("DONATE_ARMY_TG_MUSIC_PLAYER").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("DONATE_ARMY_TG_MUSIC_PLAYER").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("DONATE_ARMY_TG_MUSIC_PLAYER.plugins").info(
        "Successfully Imported All Modules "
    )

    await userbot.start()
    await DONATE_ARMY.start()
    await DONATE_ARMY.decorators()
    LOGGER("DONATE_ARMY_TG_MUSIC_PLAYER").info(
        "DONATE_ARMY_TG_MUSIC_PLAYER STARTED SUCCESSFULLY 🕊️"
    )
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("DONATE_ARMY_TG_MUSIC_PLAYER").info(
        "Stopping DONATE_ARMY_TG_MUSIC_PLAYER! GoodBye"
    )
