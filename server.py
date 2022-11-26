import telebot
from telebot import types
from telebot.types import Message, CallbackQuery

from config import TOKEN
from qiwi import Bill


print("Бот запущен")


bot = telebot.TeleBot(TOKEN)
user = Bill()
game = {}

# Создание списков с аккаунтами.
with open("accounts/gta_accounts.txt", "r", encoding="UTF-8") as accounts:
    gta_accounts = [i for i in accounts]
with open("accounts/rust_accounts.txt", "r", encoding="UTF-8") as accounts:
    rust_accounts = [i for i in accounts]
with open("accounts/battlefield_accounts.txt", "r", encoding="UTF-8") as accounts:
    battlefield_accounts = [i for i in accounts]
with open("accounts/dota_accounts.txt", "r", encoding="UTF-8") as accounts:
    dota_accounts = [i for i in accounts]
with open("accounts/cod_accounts.txt", "r", encoding="UTF-8") as accounts:
    cod_accounts = [i for i in accounts]
with open("accounts/fortnite_accounts.txt", "r", encoding="UTF-8") as accounts:
    fortnite_accounts = [i for i in accounts]


def give_out(chat_id: int, game: dict) -> None:
    """
    Функция, использующаяся для выдачи оплаченного товара пользователю.
    :param chat_id: int (Идентификатор чата)
    :param game: dict (Словарь, ключом которого является ID пользователя, а значением - товар, который он выбрал)
    :return: None
    """
    if game == "gta":
        account = f"Ваш аккаунт: {gta_accounts[0]}"
        gta_accounts.pop(0)
    elif game == "rust":
        account = f"Ваш аккаунт: {rust_accounts[0]}"
        rust_accounts.pop(0)
    elif game == "dota":
        account = f"Ваш аккаунт: {dota_accounts[0]}"
        dota_accounts.pop(0)
    elif game == "fortnite":
        account = f"Ваш аккаунт: {fortnite_accounts[0]}"
        fortnite_accounts.pop(0)
    elif game == "cod":
        account = f"Ваш аккаунт: {cod_accounts[0]}"
        cod_accounts.pop(0)
    elif game == "battlefield":
        account = f"Ваш аккаунт: {battlefield_accounts[0]}"
        battlefield_accounts.pop(0)
    else:
        account = (
            "К сожалению, аккаунта нет. Обратитесь в поддержку и мы выдадим Вам замену."
        )
    bot.send_message(chat_id, account)


def navigation_keyboard() -> types.ReplyKeyboardMarkup:
    """
    Функция с навигационной клавиатурой. Используется для навигации по меню.
    :return: types.ReplyKeyboardMarkup
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_catalog = types.KeyboardButton("/Каталог🛒")
    button_support = types.KeyboardButton("/Поддержка🆘")
    button_profile = types.KeyboardButton("/Профиль👤")
    button_rules = types.KeyboardButton("/Правила📖")
    return keyboard.add(
        button_profile, button_catalog, button_support, button_rules, row_width=2
    )


def catalog_keyboard() -> types.InlineKeyboardMarkup:
    """
    Функция для создания клавиатуры, где пользователю предлагается выбрать интересующий товар.
    :return: types.InlineKeyboardMarkup
    """
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
def hello(message: Message) -> None:
    """
    Функция приветствия. Вызывает навигационную клавиатуру.
    :param message: Message
    :return: None
    """
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в наш магазин игровых аккаунтов!\n"
        "Для более удобной навигации рекомендуем использовать клавиатуру\nОбратите внимание, что после оплаты товара "
        'необходимо нажать на кнопку "Проверить"',
        reply_markup=navigation_keyboard(),
    )


@bot.message_handler(commands=["Каталог🛒"])
def catalog(message: Message) -> None:
    """
    Функция, запрашивающая у пользователя - какой товар его интересует.
    :param message: Message
    :return: None
    """
    bot.send_message(
        message.chat.id,
        "Пожалуйста, выберите необходимую игру:",
        reply_markup=catalog_keyboard(),
    )


@bot.message_handler(commands=["Профиль👤"])
def profile(message: Message) -> None:
    """
    Функция, выводящая пользователю информацию об аккаунте. (ID TG, @username)
    :param message: Message
    :return: None
    """
    bot.send_message(
        message.chat.id, f"ID: {message.from_user.id} | @{message.chat.username}"
    )


@bot.message_handler(commands=["Поддержка🆘"])
def support(message: Message) -> None:
    """
    Функция, отправляющая сообщение пользователю с просьбой написать проблему
    :param message: Message
    :return: None
    """
    bot.send_message(message.chat.id, "Опишите вашу проблему максимально подробно: ")
    bot.register_next_step_handler(message, support_order)


def support_order(message: Message) -> None:
    """
    Функция, сохраняющая описанную пользователем проблему в текстовый файл.
    После записи проблемы в БД отправляет сообщение об успешной записи и возвращает навигационную клавиатуру.
    :param message: Message
    :return: None
    """
    with open("support_order.txt", "a", encoding="UTF-8") as sup:
        sup.write(f"Пользователь: @{message.chat.username}\nПроблема: {message.text}\n")
    bot.send_message(
        message.chat.id,
        "Ваше обращение успешно принято в обработку.",
        reply_markup=navigation_keyboard(),
    )


@bot.message_handler(commands=["Правила📖"])
def rules(message: Message) -> None:
    """
    Функция, отправляющая пользователю правила магазина.
    :param message: Message
    :return: None
    """
    bot.send_message(
        message.chat.id,
        "1. Всегда ведите запись экрана при оплате товара, чтобы у вас были доказательства.\n"
        "2. В случае каких-то ошибок обращайтесь в Поддержку.\n"
        '3. После оплаты товара необходимо нажать кнопку "Проверить:"\n',
        reply_markup=navigation_keyboard(),
    )


@bot.callback_query_handler(func=lambda call: True)
def handle(call: CallbackQuery) -> None:
    """
    Функция, отправляющая описание товара + ссылка для оплаты.
    Здесь же находится проверка оплаты товара
    :param call: CallbackQuery
    :return: None
    """

    def keyboard_for_pay() -> types.InlineKeyboardMarkup:
        """
        Функция создания клавиатуры для оплаты товара.
        :return: types.InlineKeyboardMarkup
        """
        message_id = call.message.id
        pay_keyboard = types.InlineKeyboardMarkup()
        if call.data == "gta":
            button_pay = types.InlineKeyboardButton(
                "Оплатить", url=user.create_gta_bill(message_id)
            )
        elif call.data == "rust":
            button_pay = types.InlineKeyboardButton(
                "Оплатить", url=user.create_rust_bill(message_id)
            )
        elif call.data == "cod":
            button_pay = types.InlineKeyboardButton(
                "Оплатить", url=user.create_cod_bill(message_id)
            )
        elif call.data == "dota":
            button_pay = types.InlineKeyboardButton(
                "Оплатить", url=user.create_dota_bill(message_id)
            )
        elif call.data == "battlefield":
            button_pay = types.InlineKeyboardButton(
                "Оплатить", url=user.create_battlefield_bill(message_id)
            )
        elif call.data == "fortnite":
            button_pay = types.InlineKeyboardButton(
                "Оплатить", url=user.create_fortnite_bill(message_id)
            )
        button_check_pay = types.InlineKeyboardButton(
            "Проверить", callback_data="check_pay"
        )
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
        game[call.message.from_user.id] = "gta"
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
        game[call.message.from_user.id] = "rust"
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
        game[call.message.from_user.id] = "battlefield"
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
        game[call.message.from_user.id] = "cod"
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
        game[call.message.from_user.id] = "dota"
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
        game[call.message.from_user.id] = "fortnite"
    elif call.data == "check_pay":
        user_id = call.message.from_user.id
        chat_id = call.message.chat.id
        message_id = call.message.id
        if user.check_pay(message_id):
            bot.send_message(call.message.chat.id, f"Благодарим за покупку товара.")
            give_out(chat_id, game[user_id])
            del game[user_id]
        else:
            bot.send_message(call.message.chat.id, f"Пока что оплаты не поступало.")
