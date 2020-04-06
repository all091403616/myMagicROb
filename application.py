# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton, ParseMode

updater = Updater('953890548:AAFa7EoKu_ctMSpyqHsbpHLgay9uh0SKWXY')

MODE, BOLD, ITALIC, LINK, UMDERLINE = range(5)


def start_command(bot, update):
    try:
        b = bot.get_chat_member('-1001206881648', update.message.from_user.id)
        if b.status == 'left':
            keyboard = [
                [InlineKeyboardButton('عضویت در کانال', url='https://t.me/jok_khone')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard, one_time_keyboard=True)
            update.message.reply_text("برای استفاده از ربات لطفا در کانال زیز عضو شوید و مجددا روی /start کلیک کنید",
                                      reply_markup=reply_markup)
        else:
            keyboards = [
                [InlineKeyboardButton('متن درشت', callback_data='bold'),
                 InlineKeyboardButton('متن کج', callback_data='italic')],
                [InlineKeyboardButton('متن لینک دار', callback_data='link')],
                [InlineKeyboardButton('متن زیر خط دار', callback_data='underline')],
                [InlineKeyboardButton('تبلیغات', callback_data='ads'),
                 InlineKeyboardButton('دیگر ربات های ما', callback_data='robots')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboards, one_time_keyboard=True)
            update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
            del reply_markup
            del keyboards
            return MODE

    except Exception as ex:
        print(str(ex))


def inline_buttons(bot, update):
    query = update.callback_query
    if query.data == 'bold':
        try:
            keyboard = [
                [InlineKeyboardButton('توقف', callback_data='cancel')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text('لطفا متن خود را وارد کنید.',
                                    reply_markup=reply_markup)
            del keyboard
            del reply_markup
            return BOLD
        except Exception as ex:
            print(str(ex))
    elif query.data == 'italic':
        try:
            keyboard = [
                [InlineKeyboardButton('توقف', callback_data='cancel')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text('لطفا متن خود را وارد کنید.',
                                    reply_markup=reply_markup)
            del keyboard
            del reply_markup
            return ITALIC
        except Exception as ex:
            print(str(ex))
    elif query.data == 'underline':
        try:
            keyboard = [
                [InlineKeyboardButton('توقف', callback_data='cancel')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text('لطفا متن خود را وارد کنید.',
                                    reply_markup=reply_markup)
            del keyboard
            del reply_markup
            return UMDERLINE
        except Exception as ex:
            print(str(ex))
    elif query.data == 'link':
        try:
            keyboard = [
                [InlineKeyboardButton('توقف', callback_data='cancel')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(
                'لطفا متن و لینک خود را با فرمت زیر وارد کنید.\nخط اول: متن موردنظر\nخط دوم: لینک موردنظر\nمثال:\nگوگل\nhttps://www.google.com ',
                reply_markup=reply_markup)
            del keyboard
            del reply_markup
            return LINK
        except Exception as ex:
            print(str(ex))
    elif query.data == 'ads':
        keyboard = [
            [InlineKeyboardButton('ارتباط با مدیر', url='https://t.me/Ashoj79')],
            [InlineKeyboardButton('توقف', callback_data='cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard, one_time_keyboard=True)
        query.edit_message_text('برای تبلیغات با مدیریت ارتباط برقرار کنید',
                                reply_markup=reply_markup)
        del keyboard
        del reply_markup
        return MODE
    elif query.data == 'robots':
        keyboard = [
            [InlineKeyboardButton('ربات آب و هوا فارسی', url='https://t.me/magic_txt_bot')],
            [InlineKeyboardButton('ربات دانلود از اینستاگرام', url='https://t.me/insta_down_load_bot')],
            [InlineKeyboardButton('ربات دانلود از یوتیوب', url='https://t.me/youtube_down_load_bot')],
            [InlineKeyboardButton('ربات کوتاه کننده لینک', url='https://t.me/short_url_bot')],
            [InlineKeyboardButton('ربات مترجم فارسی', url='https://t.me/fatranslator_bot')],
            [InlineKeyboardButton('توقف', callback_data='cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard, one_time_keyboard=True)
        query.edit_message_text('ربات های ما',
                                reply_markup=reply_markup)
        del keyboard
        del reply_markup
    elif query.data == 'cancel':
        keyboards = [
            [InlineKeyboardButton('متن درشت', callback_data='bold'),
             InlineKeyboardButton('متن کج', callback_data='italic')],
            [InlineKeyboardButton('متن لینک دار', callback_data='link')],
            [InlineKeyboardButton('متن زیر خط دار', callback_data='underline')],
            [InlineKeyboardButton('تبلیغات', callback_data='ads'),
             InlineKeyboardButton('دیگر ربات های ما', callback_data='robots')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboards, one_time_keyboard=True)
        query.edit_message_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
        del keyboards
        del reply_markup
        return MODE


def bold(bot, update):
    keyboards = [
        [InlineKeyboardButton('متن درشت', callback_data='bold'),
         InlineKeyboardButton('متن کج', callback_data='italic')],
        [InlineKeyboardButton('متن لینک دار', callback_data='link')],
        [InlineKeyboardButton('متن زیر خط دار', callback_data='underline')],
        [InlineKeyboardButton('تبلیغات', callback_data='ads'),
         InlineKeyboardButton('دیگر ربات های ما', callback_data='robots')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboards, one_time_keyboard=True)
    bot.send_message(text='<b>' + update.message.text + '</b>', chat_id=update.message.chat.id,
                     parse_mode=ParseMode.HTML)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    return MODE


def italic(bot, update):
    keyboards = [
        [InlineKeyboardButton('متن درشت', callback_data='bold'),
         InlineKeyboardButton('متن کج', callback_data='italic')],
        [InlineKeyboardButton('متن لینک دار', callback_data='link')],
        [InlineKeyboardButton('متن زیر خط دار', callback_data='underline')],
        [InlineKeyboardButton('تبلیغات', callback_data='ads'),
         InlineKeyboardButton('دیگر ربات های ما', callback_data='robots')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboards, one_time_keyboard=True)
    bot.send_message(text='<i>' + update.message.text + '</i>', chat_id=update.message.chat.id,
                     parse_mode=ParseMode.HTML)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    del reply_markup
    del keyboards
    return MODE


def underline(bot, update):
    keyboards = [
        [InlineKeyboardButton('متن درشت', callback_data='bold'),
         InlineKeyboardButton('متن کج', callback_data='italic')],
        [InlineKeyboardButton('متن لینک دار', callback_data='link')],
        [InlineKeyboardButton('متن زیر خط دار', callback_data='underline')],
        [InlineKeyboardButton('تبلیغات', callback_data='ads'),
         InlineKeyboardButton('دیگر ربات های ما', callback_data='robots')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboards, one_time_keyboard=True)
    bot.send_message(text='<u>' + update.message.text + '</u>', chat_id=update.message.chat.id,
                     parse_mode=ParseMode.HTML)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    del reply_markup
    del keyboards
    return MODE


def link(bot, update):
    keyboards = [
        [InlineKeyboardButton('متن درشت', callback_data='bold'),
         InlineKeyboardButton('متن کج', callback_data='italic')],
        [InlineKeyboardButton('متن لینک دار', callback_data='link')],
        [InlineKeyboardButton('متن زیر خط دار', callback_data='underline')],
        [InlineKeyboardButton('تبلیغات', callback_data='ads'),
         InlineKeyboardButton('دیگر ربات های ما', callback_data='robots')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboards, one_time_keyboard=True)
    text = update.message.text.split('\n')[0]
    lin = update.message.text.split('\n')[1]
    bot.send_message(text='<a href="' + lin + '">' + text + '</a>', chat_id=update.message.chat.id,
                     parse_mode=ParseMode.HTML)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    del reply_markup
    del keyboards
    del text
    del lin
    return MODE


def cancel(bot, update):
    update.message.reply_text("عملیات متوقف شد", reply_text=ReplyKeyboardRemove())
    keyboards = [
        [InlineKeyboardButton('آب و هوا براساس نام شهر', callback_data='city')],
        [InlineKeyboardButton('آب و هوای محل من', callback_data='location')],
        [InlineKeyboardButton('تبلیغات', callback_data='ads'),
         InlineKeyboardButton('دیگر ربات های ما', callback_data='robots')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboards, one_time_keyboard=True)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    return MODE


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_command)],
    states={
        MODE: [CallbackQueryHandler(inline_buttons),
               MessageHandler(Filters.regex('^توقف$'), cancel)],
        BOLD: [MessageHandler(Filters.text, bold),
               CallbackQueryHandler(inline_buttons)],
        ITALIC: [MessageHandler(Filters.text, italic),
                 CallbackQueryHandler(inline_buttons)],
        UMDERLINE: [MessageHandler(Filters.text, underline),
                    CallbackQueryHandler(inline_buttons)],
        LINK: [MessageHandler(Filters.text, link),
               CallbackQueryHandler(inline_buttons)],
    },
    fallbacks=[CommandHandler('cancel', inline_buttons)]
)

dp = updater.dispatcher

dp.add_handler(conv_handler)

updater.start_polling()

updater.idle()
