import telebot
from telebot import types, TeleBot

bot: TeleBot = telebot.TeleBot('6968998494:AAFx6UP1LufSDnn3dNJbYU3B8zue4uy85XI')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    # первый уровень
    markup.add(types.InlineKeyboardButton('Рентген', callback_data='xray'))
    markup.add(types.InlineKeyboardButton('Логотип', callback_data='logo'))
    markup.add(types.InlineKeyboardButton('Ответы на заявки', callback_data='tickets'))
    markup.add(types.InlineKeyboardButton('Thunderbird', callback_data='thunder'))
    markup.add(types.InlineKeyboardButton('Касса', callback_data='kassa'))
    bot.send_message(message.chat.id, f'Привет, выбери категорию:', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_query(callback):
    photo = open('./xray.jpg', 'rb')
    photo1 = open('./thunder.jpg', 'rb')
    photo2 = open('./thunder2.jpg', 'rb')
    photo3 = open('./thunder3.jpg', 'rb')
    xrayresponse = ('Ошибка <b>"Детектор не подключен":</b> \n1. Проверяем брандмауэр, он должен быть везде отключен. '
                    '\n2. Если брандмауэр включен, то отключаем его через локальную политику.')
    ticketsresponse = ('<b>1. Если мы не знаем время, в течение которого можем решить задачу:</b>'
                       '\nВрач, добрый день. \nМы уже начали работать над вашей заявкой. '
                       '\nЕсли нам потребуется дополнительная информация, мы свяжемся с вами по указанным '
                       'контактным данным. \n<b>2. Если знаем, в течение какого времени решим задачу:</b> '
                       '\nДобрый день, Врач. \nВаша заявка в работе и будет решена в течение ХХ** часов. \nЕсли нам '
                       'потребуется дополнительная информация, мы свяжемся с вами по указанным контактным данным. Вы '
                       'всегда можете узнать актуальный статус по вашему запросу по телефону 8 800 333 66 74. '
                       '\n<b>3.Если заявка по Медиалогу и мы не можем ничего сделать:</b> \nВрач, добрый день.'
                       '\nЗаявка передана в отдел поддержки бизнес-приложений (Краславскому Евгению и Анне Шипицыной). '
                       'Если ответ не поступит в течение суток, пожалуйста, свяжитесь с нами по телефону '
                       '8-800-333-66-74.')
    typekassa = ('<b>Установить тип кассы по умолчанию</b> \n1. Заходим с галочкой "Администратор".\n2. Настройки - '
                 'Настройка модулей - АРМ кассира. \n3. Выбрать Штрих-М, пароль администратора - <b>30</b>.'
                 '\n4. Сохранить и перезайти под пользователем. \n5. Пользователь - Личные настройки - ККМ - поставить '
                 'галочку Кассапэй')
    if callback.data == 'xray':
        bot.send_message(callback.message.chat.id, xrayresponse, parse_mode='html')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'logo':
        bot.send_message(callback.message.chat.id, text='<b>Для возврата логотипа:</b> \n1. Перезагрузить компьютер. '
                                                        '\n2. Обновить политики: <i>cmd (admin) - gpupdate/force</i>',
                         parse_mode="html")
    elif callback.data == 'tickets':
        bot.send_message(callback.message.chat.id, ticketsresponse, parse_mode='html')
    elif callback.data == 'thunder':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Ручная настройка', callback_data='btn1'))
        markup.add(types.InlineKeyboardButton('Почтовый клиент по умолчанию', callback_data='btn2'))
        markup.add(types.InlineKeyboardButton('Очистить память', callback_data='btn3'))
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == 'btn1':
        bot.send_message(callback.message.chat.id, "Имя пользователя может быть другим, пока такая проблема "
                                                   "была замечена только у no-reply@vetcentr.ru")
        bot.send_photo(callback.message.chat.id, photo1)
    elif callback.data == 'btn2':
        bot.send_message(callback.message.chat.id, 'Если при отправке писем из Медиалога появляется ошибка'
                                                   '"Не установлен почтовый клиент по умолчанию", то проверяем '
                                                   'следующий параметр:')
        bot.send_photo(callback.message.chat.id, photo2)
    elif callback.data == 'btn3':
        bot.send_message(callback.message.chat.id, 'Если забилась память на компьютере, то это - вина тандера, '
                                                   'so: \n1. Переходим '
                                                   'по пути C:/Users/useryouneed/AppData/Roaming/Thunderbird.'
                                                   '\n2. Удаляем выделенные файлы и настраиваем почтовый клиент')
        bot.send_photo(callback.message.chat.id, photo3)
    elif callback.data == 'kassa':
        bot.send_message(callback.message.chat.id, typekassa, parse_mode='html')


bot.polling(none_stop=True)
