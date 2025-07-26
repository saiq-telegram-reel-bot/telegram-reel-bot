import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Bot Token (keep it secret in real project using secrets)
BOT_TOKEN = "8406788064:AAEpapSvNgpzbCcrO6POwXhC3YlQL9LdBoA"

app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ooo mere शोहर 💖! Main zinda hoon, reel ya link bhejo mujhe!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "instagram.com" in text or "youtu" in text:
        await update.message.reply_text("Link mila baby 😍 — abhi download wala feature aa raha hai 💋")
    else:
        await update.message.reply_text("Yeh to reel link nahi lag raha mere जानू 🥺")

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    print("Bot running... mere शोहर ke liye 💖")
    app.run_polling()
