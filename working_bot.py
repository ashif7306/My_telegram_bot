from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am ready!')

if __name__ == '__main__':
    app = ApplicationBuilder().token('8912243117:AAE7in2ClnwHE7A3_cdOMfqmt2kVVxeLsb8').build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()