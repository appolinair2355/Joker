#!/usr/bin/env python3
"""
Fichier principal du bot Joker 3K pour Render.com (Webhook Flask)
"""
import os
import logging
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from prediction_handler import handle_prediction
from utils import is_message_finalized

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

app = Flask(__name__)
bot = Bot(token=TOKEN)
application = Application.builder().token(TOKEN).build()

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    await application.process_update(update)
    return "ok"

# Handler principal des messages
async def message_handler(update: Update, context):
    if not update.message:
        return
    text = update.message.text or ""
    if not is_message_finalized(text):
        return
    await handle_prediction(update, context)

application.add_handler(MessageHandler(filters.ALL, message_handler))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    application.run_polling()
