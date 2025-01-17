# credits: https://github.com/SpEcHiDe/PyroGramBot/pull/34


from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.helper_functions.cust_p_filters import (
    admin_fliter
)


COMMAND_HAND_LER = "/"

@Client.on_message(
    filters.command(["pin"], COMMAND_HAND_LER) &
    admin_fliter & filters.group
)
async def pin(_, message: Message):
    if not message.reply_to_message:
        try:
          await message.reply_to_message.pin()
    except:
        pass
    return True, "Succes"

@Client.on_message(
    filters.command(["unpin"], COMMAND_HAND_LER) &
    admin_fliter & filters.group
)
async def unpin(_, message: Message):
    if not message.reply_to_message:
        try:
          await message.reply_to_message.unpin()
    except:
        pass
    return True, "Succes"
