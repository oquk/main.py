import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.constants import ParseMode

# Вставьте сюда ваш токен
TOKEN = "7497722074:AAEfnNFa4dGbyqm5Iibnyia7aK4rE9kzrCo"

def generate_order_number() -> str:
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user if update.message else update.callback_query.from_user
    username = f"@{user.username}" if user.username else "покупатель"
    message = (
        f"👋 Привет, {username}!\n"
        "Ты попал в бот для покупки аккаунтов с лимитами Яндекс Сплит.\n\n"
        "Основной канал: @yandexsplit24\n"
        "Канал с отзывами: @yandexsplitreviews\n\n"
        "Навигация в боте происходит при помощи кнопок."
    )
    keyboard = [
        [InlineKeyboardButton("Профиль", callback_data='profile')],
        [InlineKeyboardButton("Ассортимент", callback_data='assortment')],
        [InlineKeyboardButton("Цены", callback_data='prices')],
        [InlineKeyboardButton("Покупка", callback_data='buy')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text(message, reply_markup=reply_markup)
    else:
        await update.callback_query.message.reply_text(message, reply_markup=reply_markup)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'profile':
        message = "Список выполненных заказов:\n1."
        keyboard = [[InlineKeyboardButton("Назад", callback_data='back')]]
    elif query.data == 'assortment':
        message = (
            "1️⃣ Аккаунт Яндекс Сплит.\nЛимит: 100.000. Прогретый аккаунт.\nЦена: 10к руб.\nВ наличии 12 штук.\n\n"
            "2️⃣ Аккаунт Яндекс Сплит.\nЛимит: 75.000. Прогретый аккаунт.\nЦена: 8к руб.\nВ наличии 7 штук.\n\n"
            "3️⃣ Аккаунт Яндекс Сплит.\nЛимит: 50.000. Прогретый аккаунт.\nЦена: 6к руб.\nВ наличии 18 штук.\n\n"
            "4️⃣ Аккаунт Яндекс Сплит.\nЛимит: 35.000. Прогретый аккаунт.\nЦена: 4к руб.\nВ наличии 32 штуки.\n\n"
        )
        keyboard = [[InlineKeyboardButton("Назад", callback_data='back')]]
    elif query.data == 'prices':
        message = (
            "Лимит 100.000 — 10к руб.\n"
            "Лимит 75.000 — 8к руб.\n"
            "Лимит 50.000 — 6к руб.\n"
            "Лимит 35.000 — 4к руб."
        )
        keyboard = [
            [InlineKeyboardButton("Купить товар", callback_data='buy')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data == 'buy':
        message = (
            "1️⃣ Аккаунт Яндекс Сплит.\nЛимит: 100.000. Прогретый аккаунт.\nЦена: 10к руб.\nВ наличии 12 штук.\n\n"
            "2️⃣ Аккаунт Яндекс Сплит.\nЛимит: 75.000. Прогретый аккаунт.\nЦена: 8к руб.\nВ наличии 7 штук.\n\n"
            "3️⃣ Аккаунт Яндекс Сплит.\nЛимит: 50.000. Прогретый аккаунт.\nЦена: 6к руб.\nВ наличии 18 штук.\n\n"
            "4️⃣ Аккаунт Яндекс Сплит.\nЛимит: 35.000. Прогретый аккаунт.\nЦена: 4к руб.\nВ наличии 32 штуки.\n\n"
        )
        keyboard = [
            [InlineKeyboardButton("1", callback_data='select_1')],
            [InlineKeyboardButton("2", callback_data='select_2')],
            [InlineKeyboardButton("3", callback_data='select_3')],
            [InlineKeyboardButton("4", callback_data='select_4')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data in ['select_1', 'select_2', 'select_3', 'select_4']:
        message = (
            "❤️ Для оплаты выбранного Вами товара, есть несколько способов:\n\n"
            "1️⃣ Банковский перевод\n\n"
            "2️⃣ Крипта\n\n"
            "Выберите удобный Вам способ."
        )
        keyboard = [
            [InlineKeyboardButton("Банковский перевод", callback_data='bank_transfer')],
            [InlineKeyboardButton("Крипта", callback_data='crypto')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data == 'bank_transfer':
        message = (
            "❤️ Оплатите сумму покупок по переводу на кошелек ЮMoney.\n\n"
            "1️⃣ Юmoney\n"
            "Номер счета:\n"
            "4100118744115724\n\n"
            "После оплаты, нажмите кнопку «Подтвердить».\n\n"
            "Инструкция по оплате через Юmoney находится в канале: @yandexsplit24"
        )
        keyboard = [
            [InlineKeyboardButton("✅ Подтвердить", callback_data='confirm')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data == 'crypto':
        message = "❤️ Выберите монету и сеть для оплаты."
        keyboard = [
            [InlineKeyboardButton("BTC", callback_data='crypto_btc')],
            [InlineKeyboardButton("USDT TRC20", callback_data='crypto_usdt_trc20')],
            [InlineKeyboardButton("USDT BEP20", callback_data='crypto_usdt_bep20')],
            [InlineKeyboardButton("SOL", callback_data='crypto_sol')],
            [InlineKeyboardButton("ETH", callback_data='crypto_eth')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data == 'crypto_btc':
        message = (
            "❤️ Оплатите сумму покупок по переводу на кошелек BTC:\n"
            "bc1qtr7hgspczl5ke89h2hdmqzt8wx7gmta2zr36re\n\n"
            "После оплаты, нажмите кнопку «Подтвердить»."
        )
        keyboard = [
            [InlineKeyboardButton("✅ Подтвердить", callback_data='confirm')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data == 'crypto_usdt_trc20':
        message = (
            "❤️ Оплатите сумму покупок по переводу на кошелек USDT TRC20:\n"
            "TBPU4Lb12GoECBiqhutNTgp7ec1SrQ22nD\n\n"
            "После оплаты, нажмите кнопку «Подтвердить»."
        )
        keyboard = [
            [InlineKeyboardButton("✅ Подтвердить", callback_data='confirm')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data == 'crypto_usdt_bep20':
        message = (
            "❤️ Оплатите сумму покупок по переводу на кошелек USDT BEP20:\n"
            "0x4FFb2270D0342023B49C71fAB9B135813a4071D0\n\n"
            "После оплаты, нажмите кнопку «Подтвердить»."
        )
        keyboard = [
            [InlineKeyboardButton("✅ Подтвердить", callback_data='confirm')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data == 'crypto_sol':
        message = (
            "❤️ Оплатите сумму покупок по переводу на кошелек SOLANA:\n"
            "FxmaQDfa87Z1qMN7u6KPvTkxCKWBMtcGhXju2eorr21b\n\n"
            "После оплаты, нажмите кнопку «Подтвердить»."
        )
        keyboard = [
            [InlineKeyboardButton("✅ Подтвердить", callback_data='confirm')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data == 'crypto_eth':
        message = (
            "❤️ Оплатите сумму покупок по переводу на кошелек ETH:\n"
            "0x4FFb2270D0342023B49C71fAB9B135813a4071D0\n\n"
            "После оплаты, нажмите кнопку «Подтвердить»."
        )
        keyboard = [
            [InlineKeyboardButton("✅ Подтвердить", callback_data='confirm')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
    elif query.data == 'confirm':
        order_number = generate_order_number()
        message = (
            "Ваш заказ передан в исполнение.\n"
            "Для получения данных от аккаунта, пишите в техподдержку нашего магазина: @yandexsplitsupport_bot\n\n"
            "В случае не оплаты товара, Вы его не получите.\n"
            "Модератор в праве попросить доказательства оплаты.\n\n"
            f"Ваш номер заказа: {order_number}"
        )
        keyboard = [[InlineKeyboardButton("Назад", callback_data='back')]]
        await query.message.reply_text(message, reply_markup=InlineKeyboardMarkup(keyboard))
        return
    elif query.data == 'back':
        await start(update, context)
        return

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(message, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_button))

    application.run_polling()

if __name__ == '__main__':
    main()
