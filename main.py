from aiogram.utils import executor #исполнитель
from commands import dp

async def bot_start(_):
    print('Бот запущен!')

executor.start_polling(dp, skip_updates=True, on_startup = bot_start) #метод, начинает прослушивание