import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import base

db = base.DataBase('ROBOT.db')

API_TOKEN = '5981320079:AAHueyIExH8O6VQNJPmH5UIpSOhGGYLkfwk'
logging.basicConfig(level=logging.INFO,filename='logs.txt')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def starter(_):
    print('Loaded !!')
async def end(_):
    print('Server Has been stopped !!')

def register(message: types.Message):
    if not db.is_joined(message.from_user.id):
        name = db.get_name(message.from_user.id)
        if type(name) == type(None):
            mt = str(message.text)
            if mt.isalpha():
                db.set_name(message.from_user.id, mt)
                return f'{mt}\nFamiliyangizni kiriting.'
            else:
                return 'Ismingizni to\'g\'ri kiriting !!!'

        surname = db.get_surname(message.from_user.id)
        if type(surname) == type(None):
            mt = str(message.text)
            if mt.isalpha():
                db.set_surname(message.from_user.id, mt)
                return f'{name} {mt}\nTelefon raqamingizni kiriting.', kb.keyboard1
            else:
                return 'Familiyangizni to\'g\'ri kiriting !!!'
        phone = db.get_phone(message.from_user.id)
        if type(phone) == type(None):
            return 'Raqamingizni kiriting', kb.keyboard1

        level = db.get_level(message.from_user.id)
        if type(level) == type(None):
            mt = str(message.text)
            if mt.lower() in kb.buttons:
                db.set_level(message.from_user.id, mt)
                db.joined(message.from_user.id)

                name = db.get_name(message.from_user.id)
                surname = db.get_surname(message.from_user.id)
                phone = db.get_phone(message.from_user.id)
                level = db.get_level(message.from_user.id)
                return f"""
                
                Siz ro\'yhatga olindingiz.\nRahmat.

                <code>Malumotlar
                Ism: {name}
                Familiya: {surname}
                Tel.Raqam: {phone}
                Dajara: {level}</code>

                """ 
            else:
                return 'Darajangizni kiriting'
        return f"""Siz ro'yhatga olingansiz!
<code>Malumotlar
Ism: {name}
Familiya: {surname}
Tel.Raqam: {phone}
Dajara: {level}</code>"""
    else:
        name = db.get_name(message.from_user.id)
        surname = db.get_surname(message.from_user.id)
        phone = db.get_phone(message.from_user.id)
        level = db.get_level(message.from_user.id)

        return f"""Siz ro'yhatga olingansiz!
<code>Malumotlar
Ism: {name}
Familiya: {surname}
Tel.Raqam: {phone}
Dajara: {level}</code>"""
    return '<code>Uzr! Xatolik yuz berdi.</code>'

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if (not db.user_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Salom')
        await bot.send_message(message.from_user.id, 'Registratsiyaga Xush Kelibsiz')
        await bot.send_message(message.from_user.id, 'Registratsiyani boshlasak')
        await bot.send_message(message.from_user.id, 'Ismingizni kiriting.')

        db.add_user(message.from_user.id)

    else:
        res = register(message)
        if type(res) in (tuple, list):
            await message.reply(res[0], reply_markup=res[1], parse_mode='html')
        else:
            await message.reply(res, parse_mode='html')

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def input_num(message: types.Message):
    phone = db.get_phone(message.from_user.id)
    if type(phone) == type(None):
        db.set_phone(message.from_user.id, str(message.contact.phone_number))
        await message.reply('''Raqam uchun rahmat.
Iltimos darajangizni kiriting.''', reply_markup=kb.keyboard2)
    else:
        await message.reply('Raqamingizni olib bo\'lganmiz.')

@dp.message_handler()
async def bot_message(message: types.Message):
    res = register(message)
    if type(res) in [tuple, list]:
        await message.reply(res[0], reply_markup=res[1], parse_mode='html')
    else:
        await message.reply(res, parse_mode='html')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,on_startup=starter,on_shutdown=end)
