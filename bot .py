from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📚 Barnoota", "ℹ️ Odeeffannoo"],
        ["❌ Exit"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Baga nagaan dhuftan 👋\nFilannoo tokko fili 👇",
        reply_markup=reply_markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Barnoota":
        keyboard = [
            ["Python Beginner"],
            ["Python Intermediate"],
            ["Python Advanced"],
            ["⬅️ Deebi'i"]
        ]
        await update.message.reply_text(
            "Sadarkaa barnootaa fili 👇",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    elif text == "Python Beginner":
        await update.message.reply_text(
            "🐍 Python Beginner\n\n"
            "Afaan Oromo:\nhttps://link.camscanner.com/5tsOFwq24j\n\n"
            "English:\nhttps://link.camscanner.com/nxk5jCGre"
        )

    elif text == "Python Intermediate":
        await update.message.reply_text(
            "⚙️ Python Intermediate\n\n"
            "Barnootni kun amma qophaa’aa jira ⏳"
        )

    elif text == "Python Advanced":
        await update.message.reply_text(
            "🚀 Python Advanced\n\n"
            "Barnootni kun fuulduratti ni dabalama 🔜"
        )

    elif text == "ℹ️ Odeeffannoo":
        await update.message.reply_text(
            "Bot kun barnoota Python kutaa kutaan kenna.\n"
            "Galatoomi fayyadamuu keetiif 🙏"
        )

    elif text == "⬅️ Deebi'i":
        await start(update, context)

    elif text == "❌ Exit":
        await update.message.reply_text("Nagaan turaa 👋")

def main():
    app = ApplicationBuilder().token("8457892076:AAEdK4EnSiCpBuC623CdQtV__-OG6xtQEd8").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("Bot hojjechaa jira...")
    app.run_polling()

if __name__ == "__main__":
    main()
