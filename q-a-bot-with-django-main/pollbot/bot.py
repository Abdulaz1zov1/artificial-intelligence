from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from random import sample
import sys, os, django
from asgiref.sync import sync_to_async


path_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from pollbot.models import Poll

def get_polls(count):
    data = Poll.objects.all()[:count]
    return [{str(i.id): {"is_answared": False, "is_correct": False}} for i in data]

def get_poll(id):
    data = Poll.objects.get(id=id)
    return data


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE, chat_data=True) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Boshlash 🔥", callback_data='start'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(f"Assalomu alaykum, Qiziqarli savol\
        javob botiga hush kelibsiz, \
        savol javoblar siz uchun qiziqmi? unda boshladik...", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE, chat_data=True) -> None:

    call_query = update.callback_query
    user_id = call_query.from_user.id
    
    query = call_query.data
    splitted_query = query.split("_")
    
    if query == "start":
        data = await sync_to_async(get_polls, thread_sensitive=True)(5)
        context.user_data['polls'] = data

        for i in data:
            value, id = list(i.values())[0]['is_answared'], list(i.keys())[0]
            if not value:
                first_poll = await sync_to_async(get_poll, thread_sensitive=True)(int(id))
                question = first_poll.question
                keyboard = [[InlineKeyboardButton(j, callback_data=f"answer_{id}_{j}")] for j in first_poll.options.split(",")]
                break
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(user_id, question, reply_markup=reply_markup)


    if splitted_query[0]=="answer":
        print(context.user_data['polls'], "o'zgarishidan oldin")
        
        current_poll = await sync_to_async(get_poll, thread_sensitive=True)(int(splitted_query[1]))
        is_correct = current_poll.correct_answer == splitted_query[2]

        for poll in context.user_data['polls']:
            poll_id = list(poll.keys())[0]
            if poll_id == splitted_query[1]:
                poll_data = list(poll.values())[0]
                poll_data['is_answared'] = True
                if is_correct:
                    poll_data['is_correct'] = True

        print(context.user_data['polls'], "o'zgargandan keyingisi")
        for i in context.user_data['polls']:
            value, id = list(i.values())[0]['is_answared'], list(i.keys())[0]
            if not value:
                first_poll = await sync_to_async(get_poll, thread_sensitive=True)(int(id))
                question = first_poll.question
                keyboard = [[InlineKeyboardButton(j, callback_data=f"answer_{id}_{j}")] for j in first_poll.options.split(",")]
                break
    
        reply_markup = InlineKeyboardMarkup(keyboard)
        await call_query.edit_message_text(question, reply_markup=reply_markup)


app = ApplicationBuilder().token("6316462566:AAExX-NYsNRE-HPlPFASTdslqelpRCjv6Ds").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()