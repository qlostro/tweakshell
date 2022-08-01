import feedbacks
import telebot
import feedbacks

bot = telebot.TeleBot('5305738144:AAGuTx4d5rl03IeeCv4TuNuKpOFzXn0Xhfc', parse_mode="html")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<i><b>Hi everyone!\nThankyou for using this Telegram bot.</b>\nTo see prices check <b>/prices</b>\nTo leave feedback type <b>/feedback</b>\nTo see older feedbacks type <b>/old</b></i>')

@bot.message_handler(commands=['prices'])
def prices(message):
    bot.send_message(message.chat.id, "There's 5 types of optimizations \n➡️FPS only - 3$\n·Takes 15-30 mins\n ·Optimizating ur game and PC\n ·+100-200 fps(my experience)\n\n ➡️ PING only- 5$\n·Takes 20-40 mins(depends on connection)\n · - 10-30 ping (maybe more)\n·Increase network speed.\n\n➡️ LATENCY ONLY-7$ (HIGLY RECOMMENDED)\n·10-15 mins\n·Game feels WAY smoother\n·Really worth it \n\n ➡️DELAY only - 5$ (recommended)\n ·Takes 5-20 mins\n ·Helps really good\n ·Suggested with LATENCY pack.\n\n ➡️Overclock(GPU)- 2$\n ·+10-70FPS \n\n ➡️ Internet pack - 15$(DELAY, LATENCY, PING) \n\n ➡️ ALL IN ONE(Absolutly everything + some bonuses) - 20$\n\n ➡️Buy sowtware i use - 40$ \n\n\n BIG notice - boost DON'T include sowtware. \nEverything is in TeamViewer. \n If pc doesn't work properly after week, 1.5x money back ")

@bot.message_handler(commands=['feedback'])
def feedback(message):
    bot.send_message(message.chat.id, 'Enter your feedback(NO emojis):')
    bot.register_next_step_handler(message, handle)

@bot.message_handler(commands=['old'])
def old(message):
    feedbacks.rfeedbacks()
    oldstuff = feedbacks.rfeedbacks()
    bot.send_message(message.chat.id, f'<b>All older feedbacks</b>:\n <i>{oldstuff}</i>')
def handle(message):
    feedbac =str(message.text)
    user = message.from_user.username
    feedbacks.add_feedback(user, 'TG', feedbac)
    bot.send_message(message.chat.id, '<b>Thank you for leaving feedback </b>\n ▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█')

bot.infinity_polling()