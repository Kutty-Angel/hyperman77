# Copyright (©️) @M8N_OFFICIAL
# By : Pavan Magar

from pyrogram import Client
from m8n.tgcalls import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from m8n.config import (
    BOT_USERNAME,
)

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi👋 I'm 𝐌𝐚𝐫𝐬𝐡𝐚𝐥𝐥 Assistant, Didn't Have A Time To Talk With You 🙂 So Kindly Join @DuskyBotZSupport For Getting Support\n\nPowered By @DuskyBotZUpdates")
  return
