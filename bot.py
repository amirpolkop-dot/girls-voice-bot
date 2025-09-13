import telebot
from telebot import types

# 🔹 اینجا توکن خودتو بذار
TOKEN = "توکن_خودت_اینجا"
bot = telebot.TeleBot(TOKEN)

approved_users = set()

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    user_id = message.from_user.id
    approved_users.add(user_id)
    bot.reply_to(message, "💖 مرسی ویس فرستادی! الان می‌تونی تو گروه پیام بدی 🌸")

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    if message.chat.type in ["group", "supergroup"]:
        if message.from_user.id not in approved_users:
            try:
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, "✨ خوش اومدی قشنگم... اول یه ویس بده بعد می‌تونی تو گروه حرف بزنی 🎤💕")
            except:
                pass

print("ربات روشن شد ✅")
bot.polling()