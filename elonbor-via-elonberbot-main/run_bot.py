from telegram import (Update, InlineKeyboardButton, InlineKeyboardMarkup,
                            ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove)

from telegram.constants import ParseMode
from telegram.ext import (ApplicationBuilder, CommandHandler,
                                ContextTypes, CallbackQueryHandler,
                                MessageHandler, filters)
from asgiref.sync import sync_to_async

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()

from django.core.files import File
from config import settings
from elon.models import Elon, ELON_TURI



async def start_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Assalomu alaykum {update.effective_user.first_name}, "\
                                "E\'lon berish uchun /elon buyrug\'rini bering")


async def elon_starter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard =[
            [InlineKeyboardButton(i[1], callback_data=i[0])] for i in ELON_TURI
        ]

    buttons = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("E'loningiz mos bo'lgan bo'limni tanlang: ", reply_markup=buttons)


async def set_category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    query = update.callback_query.data
    context.user_data['step'] = 2
    context.user_data['elon'] = {
        "category": query,
    }
    await update.callback_query.edit_message_text("Saqlandi ✅\n\nMarhamat e'lon nomini kiriting!")


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message

    if context.user_data.get("step", None)==2:
        context.user_data['step'] = 3
        context.user_data['elon']["name"] = message.text

        button = [[KeyboardButton("Mobile raqam jo'natish", request_contact=True), ]]
        
        await message.reply_text("Saqlandi ✅\n\nMarhamat mobil raqamingizni yuboring!",
                            reply_markup=ReplyKeyboardMarkup(button))
    
    elif context.user_data.get("step", None)==4:
        context.user_data['step'] = 5
        context.user_data['elon']["addition_info"] = message.text
        await message.reply_text("Saqlandi ✅\n\nMarhamat e'lon uchun rasm yuboring!", reply_markup=None)



async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message

    if context.user_data.get("step", None)==3:
        context.user_data['step'] = 4
        context.user_data['elon']["phone"] = message.contact.phone_number

    await message.reply_text("Saqlandi ✅\n\nMarhamat e'lon uchun qo'shimcha ma'lumot yuboring!",
                                            reply_markup=ReplyKeyboardRemove())


@sync_to_async
def add_object(data):
    try:
        elon = Elon(name=data['name'], etype=data['category'], contact=data['phone'],
                additional_info=data['addition_info'], photo=File(open(data['photo'], 'rb')))
        os.remove(data['photo'])
        elon.save()
        return elon
    except:
        return False


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if context.user_data.get("step", None)==5:
        photo = await message.photo[-1].get_file()
        await photo.download(f"files/{message.photo[-1].file_unique_id}.jpeg")

        context.user_data['elon']['photo'] = f"files/{message.photo[-1].file_unique_id}.jpeg"
        result = await add_object(context.user_data['elon'])
        category = ELON_TURI
        for i in ELON_TURI:
            if i[0]==result.etype:
                category = i[1]

        text = f"*Elon №{result.id} | {category}*\n"\
                f"*Nomi*: {result.name}\n"\
                f"*Aloqa uchun*: {result.contact}\n"\
                f"*Nomi*: {result.additional_info}"

        await context.bot.send_photo(
                                "@elonbor_bepul", 
                                message.photo[-1],
                                caption=text,
                                parse_mode=ParseMode.MARKDOWN
                            )
        if result:
            context.user_data['elon'] = None
            context.user_data['step'] = None
            await message.reply_text("Barcha ma'lumotlar muvaffaqiyatli qo'shildi ✅\n\n @elonbor_bepul kanalimizni kuzatib boring.")
        else:
            await message.reply_text("Keyinroq urinib ko'ring! Aloqa uchun: +998(90)357-26-61")
    else:
        await message.reply_text("E'lon berish uchun, /elon buyurug'ridan foydalaning!")


app = ApplicationBuilder().token(settings.BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start_function))
app.add_handler(CommandHandler("elon", elon_starter))
app.add_handler(CallbackQueryHandler(set_category))
app.add_handler(MessageHandler(filters.TEXT, message_handler))
app.add_handler(MessageHandler(filters.CONTACT, contact_handler))
app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

print("ishga tushdi...")
app.run_polling()
