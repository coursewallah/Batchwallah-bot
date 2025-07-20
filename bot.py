from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

ADMIN_ID = 5505630113
UPI_ID = "adityachaudhari9755@yblfrom"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to BatchWallah Bot!\nSend your payment screenshot and we'll verify it manually.")

def payment(update: Update, context: CallbackContext):
    user = update.message.from_user
    context.bot.send_message(chat_id=ADMIN_ID, text=f"New Payment Request\nFrom: {user.first_name} (@{user.username})\nUser ID: {user.id}\n\nMessage:\n{update.message.text}")
    update.message.reply_text("Thanks for the message! Admin will verify and send you the notes soon.")

def main():
    updater = Updater("8125827798:AAEVEfutpzDMwuAWBhrIMlxJuApOOp8ZPW4", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, payment))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
