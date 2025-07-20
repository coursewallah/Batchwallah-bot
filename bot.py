from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

ADMIN_ID = 5505630113
UPI_ID = "adityachaudhari9755@yblfrom"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BatchWallah Bot!\nSend your payment screenshot and we'll verify it manually."
    )

async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"New Payment Request\nFrom: {user.first_name} (@{user.username})\nUser ID: {user.id}\n\nMessage:\n{update.message.text}"
    )
    await update.message.reply_text(
        "Thanks for the message! Admin will verify and send you the notes soon."
    )

def main():
    app = ApplicationBuilder().token("8125827798:AAEVEfutpzDMwuAWBhrIMlxJuApOOp8ZPW4").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, payment))

    app.run_polling()

if __name__ == "__main__":
    main()
