from nonebot import get_driver

from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import (
    Bot,
    GROUP,
    Message,
    GroupMessageEvent,
    MessageSegment,
    ActionFailed
)

from .config import Config

from main_func import *

global_config = get_driver().config
config = Config.parse_obj(global_config)

gameStart = on_command("start xiuxian", permission=GROUP)
@gameStart.handle()
async def game_start_(bot: Bot, event: GroupMessageEvent):
    startGame(bot,event)    
    await gameStart.finish()