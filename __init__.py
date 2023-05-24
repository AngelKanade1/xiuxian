from nonebot import get_driver

from .config import Config
#吴冒达是个潮种
global_config = get_driver().config
config = Config.parse_obj(global_config)


