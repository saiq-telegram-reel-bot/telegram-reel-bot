import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Bot token from Render Environment Variables
BOT_TOKEN = os.environ["BOT_TOKEN"]

# Create the bot application
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey mere shohar 💖! Main zinda hoon Render pe... Reel ya link bhejo mujhe!")

# Message handler for Instagram or YouTube links
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "instagram.com" in text or "youtu" in text:
        await update.message.reply_text("Link detect kiya 😍 (Download wala feature agle version me 🛠️)")
    else:
        await update.message.reply_text("Ye toh valid link nahi baby 🥺")

# Add handlers to the app
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Run the bot using polling (recommended for free Render plan)
if __name__ == "__main__":
    print("Bot is running for you 24x7 mere shohar 💋")
    app.run_polling()
