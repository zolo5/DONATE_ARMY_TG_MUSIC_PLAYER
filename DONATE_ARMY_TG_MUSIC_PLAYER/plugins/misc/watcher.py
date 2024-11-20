from pyrogram import filters
from pyrogram.types import Message

from DONATE_ARMY_TG_MUSIC_PLAYER import app
from DONATE_ARMY_TG_MUSIC_PLAYER.core.call import DONATE_ARMY


@app.on_message(filters.video_chat_started, group=20)
@app.on_message(filters.video_chat_ended, group=30)
@app.on_message(filters.left_chat_member)
async def force_stop_stream(_, message: Message):
    try:
        if message.left_chat_member and not message.left_chat_member is None:
            if message.left_chat_member.id == (await get_assistant(message.chat.id)).id:
                return await DONATE_ARMY.force_stop_stream(message.chat.id)
        await DONATE_ARMY.force_stop_stream(message.chat.id)
    except Exception:
        pass
