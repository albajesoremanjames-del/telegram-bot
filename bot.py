import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# Get the token securely from an environment variable
TOKEN = os.environ["BOT_TOKEN"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to My Bot Generator!\n\n"
        "Available commands:\n"
        "/create - Create a bot\n"
        "/help - Show help"
    )


async def create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 Bot Generator\n\n"
        "The bot creation system will be added next!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Help\n\n"
        "/start - Start the bot\n"
        "/create - Create a bot\n"
        "/help - Show this message"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("create", create))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
