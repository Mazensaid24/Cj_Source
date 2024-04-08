import asyncio
import os
import time
import requests
import aiohttp
from strings.filters import command
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait

@app.on_message(command(["المالك", "صاحب الخرابه", "المنشي"]) & filters.group)
async def gak_owne(client: Client, message: Message):
      if len(message.command) >= 2:
         return 
      else:
            chat_id = message.chat.id
            f = "administrators"
            async for member in client.iter_chat_members(chat_id, filter=f):
               if member.status == "creator":
                 id = member.user.id
                 key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                 m = await client.get_chat(id)
                 if m.photo:
                       photo = await app.download_media(m.photo.big_file_id)
                       return await message.reply_photo(photo, caption=f"🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{m.first_name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{m.username}\n🎃 ¦𝙸𝙳 :`{m.id}`\n💌 ¦𝙱𝙸𝙾 :{m.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :`{message.chat.id}`",reply_markup=key)
                 else:
                    return await message.reply("• " + member.user.mention)
                    
                    
   

   
@app.on_message(command(["اسمي", "اسمي اي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""❤️‍🔥 اسمك »»  {message.from_user.mention()}""") 

        

SPAM_CHATS = []


@app.on_message(filters.command(["تاك", "@all"], "") & filters.group & admin_filter)
async def tag_all_users(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ") 
        return                  
    if replied:
        SPAM_CHATS.append(message.chat.id)      
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id): 
            if message.chat.id not in SPAM_CHATS:
                break       
            usernum += 5
            usertxt += f" {m.user.first_name}"
            if usernum == 1:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]
        
        SPAM_CHATS.append(message.chat.id)
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):       
            if message.chat.id not in SPAM_CHATS:
                break 
            usernum += 1
            usertxt += f" {m.user.first_name}"
            if usernum == 5:
                await app.send_message(message.chat.id,f'{text}\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""                          
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass        
           
@app.on_message(filters.command("cancel") & ~filters.private)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try :
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!")     
                                     
    else :
        await message.reply_text("ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!")  
        return


@app.on_message(command(["بس المنشن", "/cancel","بس منشن"]))
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in ["administrator", "creator"]:
    await message.reply("يجب انت تكون مشرف لاستخدام الامر 🖱️")
    return
  if message.chat.id not in array:
     await message.reply("المنشن متوقف بالفعل")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("تم ايقاف المنشن بنجاح✅")
    return


@app.on_message(filters.new_chat_members)
async def wel__come(client: Client, message: Message):
 chatid= message.chat.id
 await client.send_message(text=f"- نورت ياا فرتكهه😘🤝️ {message.from_user.mention}\n│ \n└ʙʏ في {message.chat.title}",chat_id=chatid)
 
@app.on_message(filters.left_chat_member)
async def good_bye(client: Client, message: Message):
 chatid= message.chat.id
 await client.send_message(text=f"- مشيت ليه يوحش يلا بسلامات🥲👋\n│ \n└ʙʏ  {message.from_user.mention} ",chat_id=chatid)



