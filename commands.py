from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext


def start(update, context):
    """Send a message when the command /start is issued."""
    keyboard = [
        [
            InlineKeyboardButton("minsk", callback_data='1'),
            InlineKeyboardButton("spb", callback_data='2'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('hello', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if query.data == '1':
        query.edit_message_text('minsk photographer')
    else:
        query.edit_message_text('spb photographer')


def help(update, context):
    """Send a message when the command /help is issued."""
    # update.message.reply_text('Help!')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def print_photographers(update, context):
    update.message.reply_text('print photographers')
