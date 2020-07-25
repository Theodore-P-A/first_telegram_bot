import logging
from random import randint
from aiogram import Bot, Dispatcher, executor, types
from PIL import Image
import sys
'''
Подлюченные модули:
PIL; AIOGRAM; RANDOM;
'''

API_TOKEN = '1340735721:AAEaYT3K5zrqIfmzEhAH7f3BLVikA2PX0N4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
ms = '''Привет!
Вот список доступных команд:
/help - помощь в работе с ботом
/info - информация о боте
/randpic - ты получишь случайную картинку
/couppic - случайная картинка будет перевёрнута на 180 градусов
/converter - случайную картинку конвертирует из JPG в PNG'''
mh = '''Описание работы команд:
/start - Начальная команда, запускает бота, показывает его меню
/help - Открывает меню помощи или полного описания команд
/info - Показывает описание бота
/randpic - Находит случайную картинку и отправляет пользователю
/couppic - Находит случайную картинку, переворачивает на 180 градусов, сохраняет,
 после чего отправляет пользователю
/converter - Находит случайную картинку, конвертирует из JPG в PNG, 
 сохраняет и после отправляет новый файл пользователю'''
mi = '''Name: FB
Description: Это очень молодой бот, пока что он ничего не умеет, но он учится!
About: ...В прочем тоже самое можно сказать и про его создателя )
Commands: 6 commands'''

#Команда пуска
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await message.answer(ms)

#Помощь пользователю
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
	await message.answer(mh)

#Информация для пользователя
@dp.message_handler(commands=['info'])
async def info(message: types.Message):
	with open ("Весёлый_банан.png","rb") as botpic:
		await bot.send_photo(message.from_user.id, botpic, mi)

#Отправляет случайное фото
@dp.message_handler(commands=['randpic'])
async def randpic(message: types.Message):
	x = str(randint(1,6))
	with open (x + ".jpg", "rb") as randpic:
		await bot.send_photo(message.from_user.id, randpic)

#Переворачивает фото на 180 градусов
@dp.message_handler(commands=['couppic'])
async def couppic(message: types.Message):
	x = str(randint(1,6))
	couppic = Image.open(x + ".jpg")
	rotated = couppic.rotate(180)
	rotated.save(x + "_rotated.jpg")
	with open (x + "_rotated.jpg", "rb") as coop:
		await bot.send_photo(message.from_user.id, coop)

#Конвертор JPG - PNG
@dp.message_handler(commands=['converter'])
async def converter(message: types.Message):
	x = str(randint(1,6))
	convpic = Image.open(x + ".jpg")
	convpic.save(x + "_new.png", "png")
	with open (x + "_new.png", 'rb') as convpic:
		await bot.send_photo(message.from_user.id, convpic)


executor.start_polling(dp)