import os
from dotenv import load_dotenv

load_dotenv()

ANGEL_BOT_TOKEN = os.environ['ANGEL_BOT_TOKEN']
PLAYERS_FILENAME = "player_data.csv" 
CHAT_ID_JSON = "chat_id.json"
ANGEL_ALIAS = os.environ['ANGEL_ALIAS']
MORTAL_ALIAS = os.environ['MORTAL_ALIAS']