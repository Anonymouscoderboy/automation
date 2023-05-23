import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the predefined questions and their corresponding answers in Hindi (written using English alphabets)
questions = {
    "Aapka naam kya hai?": "Mera naam hai ChatBot.",
    "Kaise ho aap?": "Main theek hoon, dhanyavaad!",
    "Samay kya hua hai?": "Vartmaan samay hai <CURRENT_TIME>.",
    "Aap kahan se hain?": "Main ChatBotland se hoon."
}


# Start command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Namaste! I am a ChatBot. How can I assist you?")


# Help command handler
def help_command(update: Update, context: CallbackContext):
    # Create keyboard with two buttons
    keyboard = [['Owner ID (@decent_op)', 'Support Group (@pglpnti_ki_duniya)']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    update.message.reply_text(
        "You can ask me questions, and I will try to answer them!",
        reply_markup=reply_markup
    )


# Message handler
def handle_message(update: Update, context: CallbackContext):
    message = update.message.text

    if message in questions:
        answer = questions[message]
        if "<CURRENT_TIME>" in answer:
            # Replace <CURRENT_TIME> placeholder with actual current time
            import datetime
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            answer = answer.replace("<CURRENT_TIME>", current_time)
        update.message.reply_text(answer)
    else:
        update.message.reply_text("Sorry, I don't know the answer to that question.")


def main():
    # Create the Telegram Updater and pass in your bot token
    updater = Updater("5058249365:AAERn1bZNpZb-LkJWSJCiKw55XIe6HXc3-s")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Register message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
