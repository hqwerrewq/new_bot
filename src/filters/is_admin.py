# from aiogram.filters import BaseFilter
# from aiogram.types import Message
# from src.settings.config import config
#
#
# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids) -> None:
#         self.admin_ids = admin_ids
#
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids
#
#
# check = IsAdmin(admin_ids=config.ADMINS_IDS)
