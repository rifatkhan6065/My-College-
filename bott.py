import logging
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(name)

# Your Telegram Bot Token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Your social media links and API tokens
SOCIAL_MEDIA_LINKS = {
    'Facebook': 'https://www.facebook.com/rifatkhan6065',
    'Instagram': 'https://www.instagram.com/see_with_rk/',
    'Threads': 'https://www.threads.net/@see_with_rk',
    'TikTok': 'https://www.tiktok.com/@rifatkhan_6065',
    'GitHub': 'https://github.com/Rifatkhan6065',
    'Blogger': 'https://rifatkhan6065.blogspot.com/',
    'Gmail': 'rifatkhan6065@gmail.com',
}

def start(update, context):
    update.message.reply_text('Hello! I am your social media sharing bot. Use /share to share your posts.')

def share(update, context):
    # Fetch the latest post from your social media platform
    # This is a dummy function, replace it with actual API calls
    latest_post = "This is the latest post from your social media!"

    # Send the post to Telegram
    for platform, link in SOCIAL_MEDIA_LINKS.items():
        context.bot.send_message(chat_id=update.message.chat_id, text=f"New post on {platform}:\n{latest_post}\n{link}")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("share", share))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if name == 'main':
    main()