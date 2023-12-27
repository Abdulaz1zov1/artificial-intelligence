from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from pprint import pprint


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.chat.id==822940840:
        await context.bot.sendMessage(1583471188, update.message.text)
    elif update.message.chat.id==1583471188:
        await context.bot.sendMessage(822940840, update.message.text)


app = ApplicationBuilder().token("6937532755:AAHUCaZF37fodBwM3UBmv_YfJesrOZ8x6d0").build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.ALL, callback=hello))

print("Ishladi...")
app.run_polling()

