import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

def get_group_id(update, context):
    chat = update.effective_chat
    if chat.type in ['group', 'supergroup']:
        group_id = chat.id
        context.bot.send_message(chat_id=chat.id, text=f"✅ Groupe détecté : `{group_id}`", parse_mode="Markdown")

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, get_group_id))

print("🤖 Bot en ligne. Envoie un message dans ton groupe Telegram...")
updater.start_polling()
