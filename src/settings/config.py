import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    API_ID = os.getenv('API_ID')
    API_HASH = os.getenv('API_HASH')
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    PHONE_NUMBER = os.getenv('PHONE_NUMBER')
    TEST_TOKEN = os.getenv('TEST_TOKEN')


config = Config()
