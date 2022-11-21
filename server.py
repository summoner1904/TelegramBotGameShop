import telebot
from telebot import types
from config import TOKEN
from qiwi import GenerateBill
bot = telebot.TeleBot(TOKEN)
user = GenerateBill()
# Клавиатуры на все случаи жизни
def navigation_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_catalog = types.KeyboardButton("/Каталог🛒")
    button_support = types.KeyboardButton("/Поддержка🆘")
    button_profile = types.KeyboardButton("/Профиль👤")
    button_rules = types.KeyboardButton("/Правила📖")
    return keyboard.add(
        button_profile, button_catalog, button_support, button_rules, row_width=2
    )


# Клавиатура для каталога (всякие игрушки)
def catalog_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_gta = types.InlineKeyboardButton("GTA V", callback_data="gta")
    button_rust = types.InlineKeyboardButton("Rust", callback_data="rust")
    button_dota = types.InlineKeyboardButton("Dota 2", callback_data="dota2")
    button_battlefield = types.InlineKeyboardButton(
        "Battlefield", callback_data="battlefield"
    )
    button_cod = types.InlineKeyboardButton("CoD", callback_data="cod")
    button_fortnite = types.InlineKeyboardButton("Fortnite", callback_data="fortnite")
    return keyboard.add(
        button_gta,
        button_rust,
        button_fortnite,
        button_cod,
        button_dota,
        button_battlefield,
        row_width=2,
    )


@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в наш магазин игровых аккаунтов!\n"
        "Для более удобной навигации рекомендуем использовать клавиатуру",
        reply_markup=navigation_keyboard(),
    )


# При нажатии на клавиатуре "Каталог"
@bot.message_handler(commands=["Каталог🛒"])
def catalog(message):
    bot.send_message(
        message.chat.id,
        "Пожалуйста, выберите необходимую игру:",
        reply_markup=catalog_keyboard(),
    )


# При нажатии на клавиатуре "Профиль"
@bot.message_handler(commands=["Профиль👤"])
def profile(message):
    bot.send_message(
        message.chat.id, f"ID: {message.from_user.id} | @{message.chat.username}"
    )


# При нажатии на клавиатуре "Поддержка"
@bot.message_handler(commands=["Поддержка🆘"])
def support(message):
    bot.send_message(message.chat.id, "Опишите вашу проблему максимально подробно: ")
    bot.register_next_step_handler(message, support_order)


def support_order(message):
    with open("support_order.txt", "a", encoding="UTF-8") as sup:
        sup.write(f"Пользователь: @{message.chat.username}\nПроблема: {message.text}\n")
    bot.send_message(
        message.chat.id,
        "Ваше обращение успешно принято в обработку.",
        reply_markup=navigation_keyboard(),
    )


# При нажатии на клавиатуре "Правила"
@bot.message_handler(commands=["Правила📖"])
def rules(message):
    bot.send_message(
        message.chat.id,
        "1. Всегда ведите запись экрана при оплате товара, чтобы у вас были доказательства.\n"
        "2.Представим, что здесь еще всякие пунктики правил\n"
        "3.Представим, что здесь еще всякие пунктики правил\n"
        "4.Представим, что здесь еще всякие пунктики правил\n"
        "5.Представим, что здесь еще всякие пунктики правил\n",
        reply_markup=navigation_keyboard(),
    )


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    if call.data == "gta":
        bill_keyboard = types.InlineKeyboardMarkup()
        button_pay = types.InlineKeyboardButton("Оплатить", url=user.create_gta_bill())
        button_check_pay = types.InlineKeyboardButton("Проверить", callback_data="check_pay")
        bill_keyboard.add(button_pay, button_check_pay)
        bot.send_photo(
            call.message.chat.id,
            photo="https://xage.ru/media/uploads/2018/04/gtav.jpg",
            caption="GTA V | "
            "249 "
            "RUB\nПлатформа: Steam\nДля оплаты товара нажмите на кнопку ниже. "
                    "У вас откроется новая вкладка, где вы сможете оплатить счёт",
            reply_markup=bill_keyboard
        )
    if call.data == "rust":

    elif call.data == "check_pay":
        user.check_gta_bill()
        if user.check_gta_bill() == "PAID":
            ###TODO
        else:
            print("Оплата пока не прошла")

print("Запущено")
bot.infinity_polling()
