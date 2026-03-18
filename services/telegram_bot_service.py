from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import os

from services.owm_service import format_response

load_dotenv()

bot_username = "weather_23123123_bot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'Holaaa {update.effective_user.first_name} introduce un nombre de ciudad')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if bot_username in text:
            new_text: str = text.replace(bot_username, '').strip()
            response: str = handle_response(new_text)
        else: return
    else:
        response: str = handle_response(text)

    print('BOT:', response)
    await update.message.reply_text(response)



def handle_response(text: str):
   procesed: str = text.lower()
   return format_response(procesed)

def init_bot():
    print('Starting bot...')
    app = ApplicationBuilder().token(os.getenv('TELEGRAM_KEY')).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.run_polling()

