import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]
WEBHOOK_URL = os.environ["WEBHOOK_URL"]  # Your public Render URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey mere shohar 💖! Main webhook se zinda hoon... Reel ya link bhejo mujhe!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "instagram.com" in text or "youtu" in text:
        await update.message.reply_text("Link detect kiya 😍 (Download feature next)")
    else:
        await update.message.reply_text("Ye valid link nahi baby 🥺")

app = ApplicationBuilder().token(BOT_TOKEN).webhook_url(WEBHOOK_URL).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    print("Bot is running via webhook... 💋")
    app.run_webhook(listen="0.0.0.0", port=10000, webhook_url=WEBHOOK_URL)
