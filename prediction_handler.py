import re
from telegram import Update
from telegram.ext import ContextTypes
from utils import extract_cards, all_cards_different, extract_message_number

PREDICTION_PREFIX = "🤖 Joker 3K 🤖\nPrévision 3K sur #n{}\nStatut:"

async def handle_prediction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    match = re.search(r"#n(\d+).*?\(([^)]+)\)", text)
    if not match:
        return
    msg_number = int(match.group(1))
    cards = extract_cards(match.group(2))
    if len(cards) == 3 and all_cards_different(cards):
        prediction_msg = PREDICTION_PREFIX.format(msg_number)
        sent = await update.message.reply_text(prediction_msg + " 🟡 En attente...")
        # Ici vous pouvez stocker sent.message_id et msg_number pour suivi
