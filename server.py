import telebot
from telebot import types
from config import TOKEN
from qiwi import Bill

bot = telebot.TeleBot(TOKEN)
user = Bill()


def give_out(call, counter):
    with open("product.txt", "r", encoding="UTF-8") as accounts:
        account = accounts.readlines()[counter]
    bot.send_message(call.message.chat.id, account)

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
    print(message.id)


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
    def keyboard_for_pay():
        message_id = call.message.id
        pay_keyboard = types.InlineKeyboardMarkup()
        if call.data == "gta":
            button_pay = types.InlineKeyboardButton("Оплатить", url=user.create_gta_bill(message_id))
        elif call.data == "rust":
            button_pay = types.InlineKeyboardButton("Оплатить", url=user.create_rust_bill(message_id))
        elif call.data == "rust":
            button_pay = types.InlineKeyboardButton("Оплатить", url=user.create_cod_bill(message_id))
        elif call.data == "rust":
            button_pay = types.InlineKeyboardButton("Оплатить", url=user.create_dota_bill(message_id))
        elif call.data == "rust":
            button_pay = types.InlineKeyboardButton("Оплатить", url=user.create_battlefield_bill(message_id))
        elif call.data == "rust":
            button_pay = types.InlineKeyboardButton("Оплатить", url=user.create_fortnite_bill(message_id))
        button_check_pay = types.InlineKeyboardButton("Проверить", callback_data="check_pay")
        return pay_keyboard.add(button_pay, button_check_pay)

    if call.data == "gta":
        bot.send_photo(
            call.message.chat.id,
            photo="https://xage.ru/media/uploads/2018/04/gtav.jpg",
            caption="GTA V | "
            "249 "
            "RUB\nПлатформа: Steam|Social Club\nДля оплаты товара нажмите на кнопку ниже. "
            "У вас откроется новая вкладка, где вы сможете оплатить счёт",
            reply_markup=keyboard_for_pay(),
        )

    elif call.data == "rust":
        bot.send_photo(
            call.message.chat.id,
            photo="https://pic.rutubelist.ru/video/48/a0/48a0ebdfc8a24d5890464bafabe79812.jpg",
            caption="RUST | "
            "199 "
            "RUB\nПлатформа: Steam\nДля оплаты товара нажмите на кнопку ниже. "
            "У вас откроется новая вкладка, где вы сможете оплатить счёт",
            reply_markup=keyboard_for_pay(),
        )

    elif call.data == "battlefield":
        bot.send_photo(
            call.message.chat.id,
            photo="http://keyplace.ru/wp-content/uploads/2019/10/bfv_theme.jpg",
            caption="BATTLEFIELD | "
            "699 "
            "RUB\nПлатформа: Origin\nДля оплаты товара нажмите на кнопку ниже. "
            "У вас откроется новая вкладка, где вы сможете оплатить счёт",
            reply_markup=keyboard_for_pay(),
        )

    elif call.data == "cod":
        bot.send_photo(
            call.message.chat.id,
            photo="https://gamebomb.ru/files/galleries/001/4/45/385757.jpg",
            caption="CoD Vanguard | "
            "699 "
            "RUB\nПлатформа: Battle.net\nДля оплаты товара нажмите на кнопку ниже. "
            "У вас откроется новая вкладка, где вы сможете оплатить счёт",
            reply_markup=keyboard_for_pay(),
        )

    elif call.data == "dota":
        bot.send_photo(
            call.message.chat.id,
            photo="https://i.postimg.cc/2y42Znym/V.png",
            caption="Dota 2 7000 PTS | "
            "3299 "
            "RUB\nПлатформа: Steam\nДля оплаты товара нажмите на кнопку ниже. "
            "У вас откроется новая вкладка, где вы сможете оплатить счёт",
            reply_markup=keyboard_for_pay(),
        )
    elif call.data == "fortnite":
        bot.send_photo(
            call.message.chat.id,
            photo="https://media.discordapp.net/attachments/571294092341018664/571425151338676224/unknown.png?width"
            "=1202&height=677",
            caption="Fortnite 200+ Skins | "
            "1799 "
            "RUB\nПлатформа: Epic Games\nДля оплаты товара нажмите на кнопку ниже. "
            "У вас откроется новая вкладка, где вы сможете оплатить счёт",
            reply_markup=keyboard_for_pay(),
        )
    elif call.data == "check_pay":
        counter = 0
        message_id = call.message.id
        if user.check_pay(message_id):
            bot.send_message(call.message.chat.id, f"Благодарим за покупку товара.")
            give_out(call, counter)
            counter += 1
        else:
            bot.send_message(call.message.chat.id, f"Пока что оплаты не поступало.")



print("Запущено")
bot.infinity_polling()
