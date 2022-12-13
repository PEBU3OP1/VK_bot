from aiogram import Bot, Dispatcher, executor, types
import string
import random


TOKEN = '5899583549:AAFbc46C0DvbG8fE6QMIYyWY34mAULYr0xM'
bot = Bot(TOKEN)
dp = Dispatcher(bot)

descrip = """
/help - пшл нхй
/pshlnhy - сам пошел, сука
"""
global cunt
cunt = 0



@dp.message_handler(commands = ['start'])
async def alph_random(message: types.Message):
    global cunt
    rnd = random.randint(1, 26)
    await message.answer(text=str(string.ascii_uppercase[rnd]))
    cunt = cunt + 1

    
@dp.message_handler(commands=['descrip'])
async def description(message: types.Message):
    await message.reply(text= descrip)



@dp.message_handler(commands=['count'])
async def count(message: types.Message):
    global cunt
    await message.answer(f'Кол-во вызовов {cunt}')
    cunt = cunt + 1


@dp.message_handler()
async def check_zero(message: types.Message):
    await message.answer("YES" if str(0) in message.text else "NO")

if __name__ == '__main__':
    executor.start_polling(dp)