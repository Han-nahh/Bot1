from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackContext
import os
import telegram
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def hey(update:Update,context:ContextTypes):
    await update.message.reply_text("What u lookin 4")


# def webhook(request):
#     bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
#     if request.method == "POST":
#         update = telegram.Update.de_json(request.get_json(force=True), bot)
#         chat_id = update.message.chat.id
#         # Reply with the same message
#         bot.sendMessage(chat_id=chat_id, text=update.message.text)
#     return "ok"

app = ApplicationBuilder().token("6108771734:AAE3rDdlsCQH06S_oYGG8g_0LmiXrBSIyS8").build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("hey",hey))
app.run_polling()