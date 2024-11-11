from aiogram.types import BotCommand


async def setup_bot_command(bot):
    bot_command = [
        BotCommand(command="/start", description='Запуск Бота'),
        BotCommand(command="/mumble", description='Наш Mumble'),
        BotCommand(command="/prime", description='Наш Mumble')
    ]
    await bot.set_my_commands(bot_command)
