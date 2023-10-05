from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO) #Логгирования телеграм боnа

start_keyboards = [
    types.KeyboardButton("О нас"),
    types.KeyboardButton("Курсы"),
    types.KeyboardButton("График работы"),
    types.KeyboardButton("Адрес")
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здраствуйте, {message.from_user.full_name}", reply_markup=start_button)
    print(message)

@dp.message_handler(text="О нас")
async def about(message:types.Message):
    await message.answer("""Образовательный центр Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым 
в 2018-ом году в Бишкеке
с целью дать возможность каждому человеку, даже без опыта в технологиях, 
гарантированно освоить IT-профессию.
""")
                         
@dp.message_handler(text="График работы")
async def scheduler_time(message:types.Message):
    await message.answer(f"{message.from_user.username} наш график работы\nПН-СБ 10:00-22:00")

@dp.message_handler(text='Адрес')
async def address(message:types.Message):
    await message.answer("Мы находимся по адрсу:\nМЫрзалы Аматов 1Б (БЦ Томирис)")
    await message.answer_location(40.51931772662277, 72.80301182274856)

executor.start_polling(dp)