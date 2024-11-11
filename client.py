from pyrogram import Client

from src.settings.config import config

client = Client("broken-butterfly",bot_token=config.BOT_TOKEN, api_id=config.API_ID, api_hash=config.API_HASH)
