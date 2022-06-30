import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from m8n.utils.filters import command

from m8n.config import BOT_USERNAME
from m8n.config import START_PIC
from m8n.config import BOT_NAME



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""Hi 👋 I'm **{BOT_NAME}**

You Can Use Kutty Angel To Play Music In Your Groups .

Use Inline Buttons Given Below To Know More About Kutty Angel !!""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❓ About", callback_data="cbabout"),
                    InlineKeyboardButton(
                        "🔰 Others", callback_data="others")
                ],
                [
                    InlineKeyboardButton(
                        "📚 Commands & Help", callback_data="cbevery")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add Me To Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        ),
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def gcstart(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"🙏 Thanks For Adding Kutty Angel In Your Group !! If You Want To Use Kutty Angel With Right Actions Promote Kutty Angel As Admin In This Chat ❤.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤖 Bot Owner", url=f"https://t.me/{OWNER_USERNAME}")
                ]
            ]
        ),
    )
