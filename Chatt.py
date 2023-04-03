import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up OpenAI API key
openai.api_key = "INSERT_YOUR_OPENAI_API_KEY_HERE"

# Set up Telegram bot token
bot_token = "INSERT_YOUR_TELEGRAM_BOT_TOKEN_HERE"
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
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the Telegram bot
updater.start_polling()
