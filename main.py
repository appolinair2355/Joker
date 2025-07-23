
import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()  # Charge les variables d’environnement du fichier .env

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Token Telegram manquant ! Assure-toi que la variable d'environnement TOKEN est bien définie.")

bot = Bot(token=TOKEN)

print("🤖 Bot initialisé avec succès !")
