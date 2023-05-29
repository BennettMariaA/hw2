import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='6049661190:AAGWaIIi3aL7wtdis3sJPEIU1VzluOIpJnY')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Добро пожаловать в викторину!")

@dp.message_handler(commands=['quiz'])
async def quiz_command(message: types.Message):
    question = "Вопрос: Какое лучшее место для отдыха?"
    answers = ["Пляж", "Горы", "Город"]
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_markup.add(*answers)
    await message.reply(question, reply_markup=keyboard_markup)

@dp.message_handler(lambda message: message.text in ["Пляж", "Горы", "Город"])
async def handle_quiz_answer(message: types.Message):
    selected_answer = message.text
    correct_answer = "Пляж"
    if selected_answer == correct_answer:
        reply_text = "Правильный ответ!"
    else:
        reply_text = "Неправильный ответ."

    await message.reply(reply_text)

@dp.message_handler(commands=['pin'])
async def pin_message(message: types.Message):
    if message.reply_to_message:
        await message.pin_chat_message(message.reply_to_message.message_id)

@dp.message_handler(lambda message: message.text.startswith("game"))
async def handle_game_message(message: types.Message):
    emojis = ["🎮", "🕹️", "🎲"]
    random_emoji = random.choice(emojis)
    await message.reply(random_emoji)

@dp.message_handler(commands=['dice'])
async def roll_dice(message: types.Message):
    player_dice = random.randint(1, 6)
    bot_dice = random.randint(1, 6)

    if player_dice > bot_dice:
        result = "Вы победили!"
    elif player_dice < bot_dice:
        result = "Бот победил!"
    else:
        result = "Ничья!"

    await message.reply(f"Вы бросили: {player_dice}\nБот бросил: {bot_dice}\n{result}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
