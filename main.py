from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from crud import check_user, create_user, get_dev_by_title_and_params
from keyboards import *
import os 
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from db import engine
import logging
from aiogram import F


load_dotenv()
logging.basicConfig(level=logging.INFO)


bot = Bot(os.getenv('TOKEN_API'))
dp = Dispatcher(bot=bot)
session = sessionmaker(bind=engine)
s = session()


@dp.message(CommandStart()) # Стартовый хендлер
async def cmd_start(ms: types.Message):

    if not(check_user(s, ms.from_user.id)):
        create_user(s, {'telid': ms.from_user.id, 'username':ms.from_user.username})
    await ms.answer('👋Привет!\n\n🤖<b>Это бот-каталог</b>, здесь ты можешь выбрать и купить самые современные и выгодные:\n\n📱 Телефоны\n\n💻 Компьютеры\n\n🤩 И другие девайсы\n\n<b>Основное меню:</b>', parse_mode=ParseMode.HTML, reply_markup=gen_start_kb())
    

@dp.callback_query(F.data == 'start')
async def fisrt_handler(callback: types.CallbackQuery):
    await callback.message.answer('👋Привет!\n\n🤖<b>Это бот-каталог</b>, здесь ты можешь выбрать и купить самые современные и выгодные:\n\n📱 Телефоны\n\n💻 Компьютеры\n\n🤩 И другие девайсы\n\n<b>Основное меню:</b>', parse_mode=ParseMode.HTML, reply_markup=gen_start_kb())


@dp.callback_query(lambda call: 'first_' in call.data)
async def fisrt_handler(callback: types.CallbackQuery):
    typ = callback.data.replace('first_', '')
    await callback.message.edit_text(f'🔎 Выберете бренд по запросу: \n\n<b>{typ}</b>', parse_mode=ParseMode.HTML, reply_markup=gen_companyies_kb(typ))


@dp.callback_query(lambda call: 'second_' in call.data)
async def second_handler(callback: types.CallbackQuery):
    cb = callback.data.replace('second_', '').split('_')
    await callback.message.edit_text(f'🔎 Все товары по вашему запросу:', parse_mode=ParseMode.HTML, reply_markup=gen_devices_kb(cb[1], cb[0], callback.data))


@dp.callback_query(lambda call: 'devs_' in call.data)
async def second_handler(callback: types.CallbackQuery):
    dev = callback.data.replace('devs_', '')
    await callback.message.edit_text(f'🔎 Все товары по вашему запросу:\n\n{dev}', parse_mode=ParseMode.HTML, reply_markup=gen_devices_param_kb(dev, callback.data))


@dp.callback_query(lambda call: 'params' in call.data)
async def last_handler(callback: types.CallbackQuery):
    dev = callback.data.replace('params_', '').split('#')
    title = dev[0]
    params = dev[1]
    dev = get_dev_by_title_and_params(s, title, params)
    await callback.message.edit_text(f'<b>{title} {params}</b>\n\nСтоимость: {dev.price} руб\n\nЧтобы купить, напишите @P1g3on', parse_mode=ParseMode.HTML, reply_markup=gen_last_kb(title))


if __name__=='__main__':
    dp.run_polling(bot)

