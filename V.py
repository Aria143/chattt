import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

# Set up OpenAI API key
openai.api_key = "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"

# Set up Telegram bot token
bot_token = "5935054751:AAG84Bhcweo3RyHjaljrs12hIEXYEHvfQxw"
bot = telegram.Bot(token=bot_token)

# Define the function that generates responses using OpenAI GPT-3
def generate_response(text):
    prompt = f"User: {text}\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Define the function that handles incoming messages from Telegram
def handle_message(update, context):
    user_text = update.message.text
    bot_text = generate_response(user_text)
    update.message.reply_text(bot_text)

# Set up the Telegram bot updater and handlers
updater = Updater(bot_token)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(None, handle_message))

# Start the Telegram bot
updater.start_polling()
