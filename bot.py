from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
from openai import AsyncOpenAI
import os

# Ambil dari Environment Variables Railway
TELEGRAM_TOKEN = os.getenv("8818117723:AAG9BF8QXBqbcW_e7wLjoYjLQEXcOvc-CfE")
GROQ_API_KEY = os.getenv("xai-6hacK8sX04kUpus6sZFkdTPy2PxdmrbI98xEnSmH9WHx0Id4rrq4x20AZfz2GqfshseV1oase9yg3YFi")

SYSTEM_PROMPT = "Kamu adalah asisten AI yang ramah, santai, helpful, dan jawab dalam bahasa Indonesia."

client = AsyncOpenAI(
    api_key=xai-6hacK8sX04kUpus6sZFkdTPy2PxdmrbI98xEnSmH9WHx0Id4rrq4x20AZfz2GqfshseV1oase9yg3YFi,
    base_url="https://api.groq.com/openai/v1"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Halo! Saya AI Chatbot. Mau ngobrol apa hari ini?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.message.chat_id

    await context.bot.send_chat_action(chat_id=chat_id, action="typing")

    try:
        response = await client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        ai_reply = response.choices[0].message.content
        await update.message.reply_text(ai_reply)
    except:
        await update.message.reply_text("❌ Maaf, sedang sibuk. Coba lagi nanti ya.")

async def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & \~filters.COMMAND, handle_message))

    print("🤖 Bot sedang berjalan di Railway...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
