import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autoforward
from config import Config
from Plugins import RE1TXT, RE2TXT, RE3TXT, RE4TXT, RE5TXT, RE6TXT, REPLACED1,REPLACED2,REPLACED3,REPLACED4,REPLACED5,REPLACED6

usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()
caption_text = Config.CAPTION_TEXT


@autoforward.on_message(filters.channel & (filters.document | filters.video | filters.audio ) & ~filters.edited, group=-1)
async def editing(bot, message):
      try:
         media = message.document or message.video or message.audio
         caption_text = Config.CAPTION_TEXT
      except:
         caption_text = ""
         pass 
      if (message.document or message.video or message.audio): 
          if message.caption:                        
             file_caption = f"<b>{message.caption}</b>"                
          else:
             fname = media.file_name
             filename = fname.replace("_", ".")
             file_caption = f"<b>{filename}</b>"  
              
      try:
          if caption_position == "bottom":          
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = file_caption.replace(RE1TXT, REPLACED1).replace(RE2TXT, REPLACED2).replace(RE3TXT, REPLACED3).replace(RE4TXT, REPLACED4).replace(RE5TXT, REPLACED5).replace(RE6TXT, REPLACED6) + "\n\n" + caption_text, 
                 parse_mode = "html"
             )
          elif caption_position == "top":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = caption_text + file_caption.replace(RE1TXT, REPLACED1).replace(RE2TXT, REPLACED2).replace(RE3TXT, REPLACED3).replace(RE4TXT, REPLACED4).replace(RE5TXT, REPLACED5).replace(RE6TXT, REPLACED6),
                 parse_mode = "html"
             )
          elif caption_position == "nil":
             await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.message_id,
                 caption = caption_text, 
                 parse_mode = "html"
             ) 
      except:
          pass
