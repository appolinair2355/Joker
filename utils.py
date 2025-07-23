import re

def is_message_finalized(text):
    return "✅" in text or "🔰" in text

def extract_cards(raw):
    return re.findall(r"[\dJQKA]+[♠️♥️♦️♣️]", raw)

def all_cards_different(cards):
    suits = [c[-1] for c in cards]
    return len(set(suits)) == 3

def extract_message_number(text):
    match = re.search(r"#n(\d+)", text)
    return int(match.group(1)) if match else None
