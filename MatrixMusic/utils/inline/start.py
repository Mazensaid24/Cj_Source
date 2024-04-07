from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="ᘜᖇ᥆ᥙρ", url= "https://t.me/YR_HC"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مـطـور الـسـورس", url= "https://t.me/Y_D_ll"),
            InlineKeyboardButton(text="ᘜᖇ᥆ᥙρ", url=f"https://t.me/YR_HC"), 
        ],
        [
            
            InlineKeyboardButton(text="᥉᥆ᥙᖇᥴᥱ", url=f"https://t.me/SOURCE_SOM3A") , 
        ],
    ]
    return buttons
