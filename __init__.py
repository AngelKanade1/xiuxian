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

global_config = get_driver().config
config = Config.parse_obj(global_config)

# 指令触发
gameStart = on_command("start xiuxian", permission=GROUP)
@gameStart.handle()
#GroupMessageEvent 代表只接受Group message。
async def run_xiuxian_(bot: Bot, event: GroupMessageEvent):
    #todo start game
    pass