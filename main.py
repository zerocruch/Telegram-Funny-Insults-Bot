import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

funny_insults = [
    "You're so dumb, you thought Taco Bell was a Mexican phone company.",
    "Your face looks like someone tried to put out a fire with a baseball bat.",
    "You're so ugly, you make Shrek look like Brad Pitt.",
    "You're so boring, you make watching paint dry exciting.",
    "You're so lazy, you put the 'pro' in procrastinate.",
    "You're so cheap, you'd steal a penny off a dead man's eye.",
    "You're so clueless, you don't know that your fly is down.",
    "You're so socially awkward, you make a baby look like a seasoned politician.",
    "You're so bad at jokes, your punchlines make me want to cry.",
    "You're so unoriginal, you're a carbon copy of a carbon copy.",
    "You're so full of yourself, you're like a balloon with a hole in it.",
    "You're so insignificant, you're like a grain of sand on a beach.",
    "You're so pathetic, you make a clown look like a comedian."
]

botToken = "Your Bot API Token Get One From Here : https://t.me/BotFather"

current_account_index = 0

def select_next_funny_insults():
    global current_account_index
    selected_account = funny_insults[current_account_index]
    current_account_index = (current_account_index + 1) % len(funny_insults) 
    return selected_account



bot = telebot.TeleBot(botToken)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    userID = str(call.from_user.id)
    data = call.data
    if data == 'insult':
        i1 = [[InlineKeyboardButton(text=f'Generate Funny Insults',
         callback_data=f'insult')]]
        inline_keyboard = InlineKeyboardMarkup(i1)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"{select_next_funny_insults()}"
        )
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=inline_keyboard
        )

@bot.message_handler(commands=['start'])
def start(message):
    global current_account_index
    userID = str(message.chat.id)
    i1 = [[InlineKeyboardButton(text=f'Generate Funny Insults',
     callback_data=f'insult')]]
    inline_keyboard = InlineKeyboardMarkup(i1)
    bot.send_message(userID, f"{funny_insults[current_account_index]}",
     reply_markup=inline_keyboard)
    current_account_index += 1

bot.infinity_polling()
