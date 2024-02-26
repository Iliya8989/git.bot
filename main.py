from telebot import *
from random import choice
TOKEN = '6715880721:AAE9XUHHOZBdgVAYCemJfDWjFkX5eqUZ-Vo'
bot = telebot.TeleBot(TOKEN)
key_murkup =telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_murkup.add('لبنیات','پروتین','ادویه', 'پشتیبانی👨‍💻', 'سبد خرید🛒', 'سبد خرید قبلی🛒')

first =telebot.types.InlineKeyboardButton("پشتیبانی👨‍💻", url="https://t.me/iliyakaviyani")
murkup =telebot.types.InlineKeyboardMarkup(row_width=2)
murkup.add(first)

@bot.message_handler(['start'])
def send_message(message):
    bot.send_message(message.chat.id, f'سلام دوست من به ربات فروش انلاین خوش اومدی{message.id}')
    bot.send_message(message.chat.id, ' چه جور محصولی می خوای?', reply_markup=key_murkup)
@bot.message_handler(func=lambda message:message.text == "لبنیات")
def send_message(message):
    bot.send_message(message.chat.id, """
پنیر🧀
خامه🍦
کره🧈
عسل🍯
                         """, reply_markup=lab)
lab =telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
lab.add('پنیر🧀','خامه🍦','کره🧈','عسل🍯', 'بازگشت🔙')

@bot.message_handler(func=lambda message:message.text == "پروتین")
def send_message(message):
    bot.send_message(message.chat.id, """
سوسیس🌭
گوشت🥩
مرغ🐓
""", reply_markup=por)
por =telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
por.add('سوسیس🌭','گوشت🥩','مرغ🐓', 'بازگشت🔙')
@bot.message_handler(func=lambda message:message.text == "ادویه")
def send_message(message):
    bot.send_message(message.chat.id, """
فلفل 🌶️
نمک🧂
زردچوبه🟨
""", reply_markup=advie)
advie =telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
advie.add('فلفل🌶️','نمک🧂','زردچوبه🟨','بازگشت🔙')
@bot.message_handler(func=lambda message:message.text == 'سوسیس🌭')
def send_message(message):
    bot.send_message(message.chat.id, """
سوسیس بلغاری:250000🌭
سوسیس گوشتیران:350000🌭                    
سوسیس با پنیر:170000🌭
""") 
@bot.message_handler(func=lambda message:message.text == 'گوشت🥩')
def send_message(message):
    bot.send_message(message.chat.id, """
گوشت گوساله:550000🥩
گوشت گوسفندی:680000🥩
گوشت کبابی:740000🥩

""")
@bot.message_handler(func=lambda message:message.text == 'مرغ🐓')
def send_message(message):
    bot.send_message(message.chat.id, """
مرغ تازه:98000🐓
فیله ی مرغ:195000🐓

""")
@bot.message_handler(func=lambda message:message.text == "پنیر🧀")
def send_message(message):
    bot.send_message(message.chat.id, """
70000:پنیر گچی🧀
پنیر لیقوان:80000🧀
120000:پنیر تبریزی🧀

""")
@bot.message_handler(func=lambda message:message.text == "خامه🍦")
def send_message(message):
    bot.send_message(message.chat.id, """
70000:خامه ی پاستوریزه🍦
120000:خامه محلی🍦

""")
@bot.message_handler(func=lambda message:message.text == "کره🧈")
def send_message(message):
    bot.send_message(message.chat.id, """
220000:کره محلی🧈
50000:کره پاستوریزه🧈

""")
@bot.message_handler(func=lambda message:message.text == "عسل🍯")
def send_message(message):
    bot.send_message(message.chat.id, """
300000:عسل طبیعی خلخال🍯
170000:عسل مصنوعی🍯

""")
@bot.message_handler(func=lambda message:message.text == "فلفل🌶️")
def send_message(message):
    bot.send_message(message.chat.id, """
150000:فلفل سیاه🌶️
120000:فلفل قرمز🌶️
150000:پاپریکا🌶️

""")
@bot.message_handler(func=lambda message:message.text == "نمک🧂")
def send_message(message):
    bot.send_message(message.chat.id, """
100000:نمک دریا🧂
60000:نمک نمکدان🧂

""")    
@bot.message_handler(func=lambda message:message.text == "زردچوبه🟨")
def send_message(message):
    bot.send_message(message.chat.id, """
100000:زرد چوبه🟨
""")
@bot.message_handler(func=lambda message:message.text == 'بازگشت🔙')
def send_message(message):
    bot.send_message(message.chat.id, ' چه جور محصولی می خوای?', reply_markup=key_murkup)
@bot.message_handler(func=lambda message:message.text == 'پشتیبانی👨‍💻')
def poshtiban(message):
    bot.send_message(message.chat.id, 'برای ارتباط با پشتیبانی \nروی دکمه ی زیر کلیک کن', reply_markup=murkup)
@bot.message_handler(func=lambda message:message.text == 'admin🔑')
def get_password(message):
    bot.send_message(message.chat.id, 'برای ورود رمز را وارد.')
login =telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
login.add('تغیر دیسکریپشن👨‍💻', 'بازگشت🔙')
ban =telebot.types.InlineKeyboardButton('بن کردن کاربر🔒')
mar =telebot.types.InlineKeyboardMarkup(row_width=2)
mar.add(first)
@bot.message_handler(func=lambda message:message.text == 'iliya1389'or message.text == 'login')
def send_message(message):
    chat_login ='5662227332'
    bot.send_message(message.chat.id, 'با موفقیت وارد شدید🔑', reply_markup=login)
    bot.send_message(chat_login, f'کاربر {message.chat.id}وارد شد', reply_markup=mar)
@bot.message_handler(func=lambda message:message.text == 'تغیر دیسکریپشن👨‍💻')
def namayeshi_sors(message):
    bot.send_message(message.chat.id, ' این یک دکمه  نمایشی است😂')
@bot.message_handler(func=lambda message:message.text == 'گردونه ی شانس🎯')
def gardoneg(message):
    random =random.choice("گوشت🥩", '10000موجودی کیف پول🤑', "پیک رایگان📩")
    bot.send_message(message.chat.id, f'شما برنده ی {random}شدید')
@bot.message_handler(func=lambda message:message.text == 'بن کردن کاربر🔒')
def ban(message):
    bot.ban_chat_member(message.chat.id, message.user.id)
    bot.send_message(message.chat.id, 'کاربر گرامی شما توسط ادمین بن شدید🔒')

@bot.message_handler(func=lambda message:True)
def sabad(message):
    if message.text == 'سبد خرید🛒':
        bot.send_message(message.chat.id, 'کاربر گرامی لطفا اسم محصولی که می خواید رو بنویسید:')
        bot.register_next_step_handler(message, file)
    elif message.text == 'سبد خرید قبلی🛒':
        with open(f'{message.chat.id}.txt', 'r') as f:
            s = f.read()
        bot.send_message(message.chat.id, f'سبد خرید شما🛒:\n{s}')

def file(message):
    with open(f'{message.chat.id}.txt', 'a') as f:
        f.write(message.text + '\n')

    with open(f'{message.chat.id}.txt', 'r') as f:
        s = f.read()
    bot.send_document(6795999944, open(f'{message.chat.id}.txt', 'rb'))
    bot.send_message(message.chat.id, f'سبد خرید شما🛒:\n{s}')
    f.close()

bot.infinity_polling()