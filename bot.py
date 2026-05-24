from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
from openai import AsyncOpenAI
import os

# ================== KONFIGURASI ==================
TELEGRAM_TOKEN = os.getenv("8818117723:AAG9BF8QXBqbcW_e7wLjoYjLQEXcOvc-CfE")
GROK_API_KEY = os.getenv("xai-6hacK8sX04kUpus6sZFkdTPy2PxdmrbI98xEnSmH9WHx0Id4rrq4x20AZfz2GqfshseV1oase9yg3YFi")

if not TELEGRAM_TOKEN:
    print("❌ TELEGRAM_TOKEN belum diatur!")
if not GROK_API_KEY:
    print("❌ GROK_API_KEY belum diatur!")

# Inisialisasi Grok
client = AsyncOpenAI(
    api_key=GROK_API_KEY,
    base_url="https://api.x.ai/v1"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Halo! Bot Grok AI sudah aktif.\nMau ngobrol apa saja?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.message.chat_id

    await context.bot.send_chat_action(chat_id=chat_id, action="typing")

    try:
        response = await client.chat.completions.create(
            model="grok-3",
            messages=[
                {"role": "system", "content": "Kamu adalah asisten AI yang ramah, santai, dan helpful. Jawab dalam bahasa Indonesia."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=800
        )
        await update.message.reply_text(response.choices[0].message.content)

    except Exception as e:
        print(f"ERROR: {str(e)}")
        await update.message.reply_text("❌ Maaf, bot sedang error. Coba lagi nanti.")

async def main():
    if not TELEGRAM_TOKEN or not GROK_API_KEY:
        print("❌ Konfigurasi belum lengkap. Cek Environment Variables di Railway.")
        return

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    
    # Baris ini yang sering error, kita pisah
    message_handler = MessageHandler(filters.TEXT & \~filters.COMMAND, handle_message)
    app.add_handler(message_handler)

    print("✅ Bot Grok AI berhasil dijalankan di Railway!")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())            ],
            temperature=0.7,
            max_tokens=800
        )
        ai_reply = response.choices[0].message.content
        await update.message.reply_text(ai_reply)

    except Exception as e:
        print(f"ERROR: {str(e)}")   # Ini akan muncul di Railway Logs
        await update.message.reply_text("❌ Maaf, bot sedang mengalami masalah. Coba lagi nanti.")

async def main():
    if not TELEGRAM_TOKEN or not GROK_API_KEY:
        print("❌ Konfigurasi belum lengkap!")
        return
        
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & \~filters.COMMAND, handle_message))

    print("✅ Bot Grok AI berhasil dijalankan di Railway!")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
