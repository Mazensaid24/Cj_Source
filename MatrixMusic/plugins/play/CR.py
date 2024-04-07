import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/e6f815307a347ec6e17d5.mp4",
        caption=f"""\nمرحبا بك عزيزي {message.from_user.mention} ᭙ᥱᥣ᥆ꪔᥱ ƚ᥆ ᥉᥆ᥙᖇᥴᥱ ᥉᥆ꪔ3ᥲ ꪔᥙ᥉Ꭵᥴ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᘜᖇ᥆ᥙρ", url=f"https://t.me/YR_HC"), 
                 InlineKeyboardButton(
                   "᥉᥆ᥙᖇᥴᥱ",       url=f"https://t.me/SOURCE_SOM3A"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "Ꭵ᥉ ρᎥძᥱᖇ", url=f"https://t.me/Y_D_ll"), 
                 
                ],

            ]

        ),

    )








@app.on_message(
    command(["مطور السورس","المبرمج","كريزي"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("Y_D_ll")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𝗦𝗼𝗨𝗿𝗖𝗲 𝗦𝗼𝗠𝟯𝗮 \n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\𝗦𝗼𝗨𝗿𝗖𝗲 𝗦𝗼𝗠𝟯𝗮", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["اسبايدر"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("Y_D_ll")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𝗦𝗼𝗨𝗿𝗖𝗲 𝗦𝗼𝗠𝟯𝗮 .\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n𝗦𝗼𝗨𝗿𝗖𝗲 𝗦𝗼𝗠𝟯𝗮", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



