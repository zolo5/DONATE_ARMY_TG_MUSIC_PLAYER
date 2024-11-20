#
# Copyright (C) 2024 by DONATE_ARMY™@Github, < https://github.com/DONATE-ARMY-BOTS >.
#
# This file is part of < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER > project,
# and is released under the MIT License.
# Please see < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER/blob/master/LICENSE >
#
# All rights reserved.
import aiohttp

BASE = "https://batbin.me/"


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def DONATE_ARMYbin(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    link = BASE + resp["message"]
    return link
