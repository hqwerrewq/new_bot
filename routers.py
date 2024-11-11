from aiogram import Router
from src.handlers import handler
from src.handlers.support import support


def get_apps_router():
    router = Router()
    router.include_router(handler.router)
    router.include_router(support.router)
    return router
