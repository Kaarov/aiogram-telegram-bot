from aiogram import Router

from .actions_kb_callback_handler import router as actions_kb_callback_router
from .info_kb_callback_handler import router as info_kb_callback_router

router = Router(name=__name__)

router.include_routers(
    actions_kb_callback_router,
    info_kb_callback_router,
)
