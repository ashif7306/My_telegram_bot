# bot.py
import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
GROUP1_ID = int(os.getenv("GROUP1_ID"))
GROUP2_ID = int(os.getenv("GROUP2_ID"))

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📷 Send your photo here.")

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    os.makedirs("photos", exist_ok=True)
    photo = update.message.photo[-1]
    file = await photo.get_file()
    await file.download_to_drive(f"photos/{photo.file_id}.jpg")

    await context.bot.send_photo(GROUP1_ID, photo.file_id, caption="📸 Anonymous Photo")
    await context.bot.send_photo(GROUP2_ID, photo.file_id, caption="📸 Anonymous Photo")

    await update.message.reply_text("Photo received ✅")

async def unsupported(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Please send only Photo.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, photo_handler))
app.add_handler(MessageHandler(~filters.PHOTO & ~filters.COMMAND, unsupported))

print("Bot Running...")
app.run_polling()
