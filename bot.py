import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8406788064:AAEpapSvNgpzbCcrO6POwXhC3YlQL9LdBoA"
app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey mere शोहर 💖! Main zinda hoon... Mujhe Instagram ya YouTube ka link bhejo 😘")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "instagram.com" in text or "youtu" in text:
        await update.message.reply_text("Link detect kiya 😍 (Download wala feature baad mein laayenge!)")
    else:
        await update.message.reply_text("Ye valid link nahi baby 🥺")

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    print("Bot running... mere शोहर ke liye 💖")
    app.run_polling()
