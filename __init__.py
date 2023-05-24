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

# 指令触发
gameStart = on_command("start xiuxian", permission=GROUP)
@gameStart.handle()
#GroupMessageEvent 代表只接受Group message。
async def run_xiuxian_(bot: Bot, event: GroupMessageEvent):
    back_msg = startGame()
    
    await bot.call_api('send_group_msg', **{
    'group_id': event.group_id,
    'message': back_msg
    })
    await gameStart.finish()