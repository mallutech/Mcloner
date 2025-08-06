import os
import telebot
from clone import clone_voice

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send your Malayalam reference audio to begin voice cloning.")

@bot.message_handler(content_types=['audio', 'voice'])
def handle_audio(message):
    file_info = bot.get_file(message.voice.file_id if message.voice else message.audio.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = f"ref_audio.ogg"
    with open(file_name, 'wb') as f:
        f.write(downloaded_file)

    output_path = clone_voice(file_name, "നമസ്കാരം, ഞാൻ ടെലഗ്രാമിൽ നിന്നുള്ള ഒരവതാരമാണ്.")
    with open(output_path, 'rb') as out_voice:
        bot.send_audio(message.chat.id, out_voice)

@bot.message_handler(func=lambda msg: msg.text)
def handle_text(message):
    bot.reply_to(message, "Please send a reference audio message.")

bot.polling()
