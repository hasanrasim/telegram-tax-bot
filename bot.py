from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os

# API açarlarını konfiqurasiya edin
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def start(update, context):
    update.message.reply_text('Salam! Vergi məcəlləsinə aid suallarınızı yazın.')

def handle_message(update, context):
    user_input = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=150
    )
    update.message.reply_text(response.choices[0].text.strip())

def main():
    updater = Updater(TELEGRAM_API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
