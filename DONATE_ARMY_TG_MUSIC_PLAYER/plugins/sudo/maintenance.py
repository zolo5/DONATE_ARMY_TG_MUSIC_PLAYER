#
# Copyright (C) 2024 by DONATE_ARMY™@Github, < https://github.com/DONATE-ARMY-BOTS >.
#
# This file is part of < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER > project,
# and is released under the MIT License.
# Please see < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram import filters
from pyrogram.types import Message

from DONATE_ARMY_TG_MUSIC_PLAYER import app
from DONATE_ARMY_TG_MUSIC_PLAYER.misc import SUDOERS
from DONATE_ARMY_TG_MUSIC_PLAYER.utils.database import (
    get_lang,
    is_maintenance,
    maintenance_off,
    maintenance_on,
)
from strings import get_command, get_string

# Commands
MAINTENANCE_COMMAND = get_command("MAINTENANCE_COMMAND")


@app.on_message(filters.command(MAINTENANCE_COMMAND) & SUDOERS)
async def maintenance(client, message: Message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")
    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        if await is_maintenance() is False:
            await message.reply_text("ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ")
        else:
            await maintenance_on()
            await message.reply_text(_["maint_2"])
    elif state == "disable":
        if await is_maintenance() is False:
            await maintenance_off()
            await message.reply_text(_["maint_3"])
        else:
            await message.reply_text("ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ")
    else:
        await message.reply_text(usage)
