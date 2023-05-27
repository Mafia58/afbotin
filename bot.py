from pyrogram import filters
from pyrogram import Client 
import os
import logging
logger = logging.getLogger(__name__)

app = Client("my_account")

source_channels = -1001375265989

# define the target channel to forward messages to
target_channel = -1001627061452

# Regular expression to match Telegram URL
telegram_regex = r'https?://t\.me/\w+'

#main func
@app.on_message(filters.incoming)
async def copy_handler(_, message):
    if message.chat.id == source_channels:
        
        func = await app.get_messages(source_channels,message.id)
        

        if func.photo:
            downloaded_media = []
            path = await message.download()
            
            await app.send_photo(target_channel,path,caption = func.caption )

            for path in downloaded_media:
                if os.path.isfile(path):
                    logger.debug(f"Removing file {path}")
                    os.remove(path) 

        elif func.text:
            await message.copy(target_channel)

        elif func.video:
            downloaded_media = []
            path = await message.download()
            
            await app.send_video(target_channel,path,caption = func.caption )

            for path in downloaded_media:
                if os.path.isfile(path):
                    logger.debug(f"Removing file {path}")
                    os.remove(path)    
        
        elif func.document:
            downloaded_media = []
            path = await message.download()
            
            await app.send_document(target_channel,path,caption = func.caption )

            for path in downloaded_media:
                if os.path.isfile(path):
                    logger.debug(f"Removing file {path}")
                    os.remove(path)  

        elif func.audio:
            downloaded_media = []
            path = await message.download()
            
            await app.send_audio(target_channel,path,caption = func.caption )

            for path in downloaded_media:
                if os.path.isfile(path):
                    logger.debug(f"Removing file {path}")
                    os.remove(path) 
        else:
            await message.copy(target_channel)

print("I'm Fucking Working Now!")
app.run()