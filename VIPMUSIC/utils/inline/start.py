from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="Help, callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="Set", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="Group", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝐆𝚁𝙾𝚄𝙿", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝐌ᴏʀᴇ", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="Feature", callback_data="settings_back_helper")
        ],
    ]
    return buttons
