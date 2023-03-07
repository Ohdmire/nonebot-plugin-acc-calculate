from nonebot.adapters.onebot.v11 import Event, MessageSegment, Bot
from nonebot.rule import to_me
from nonebot import on_command
from .data_source import calculate_acc
import time
from nonebot import get_driver
command_start = get_driver().config.command_start

help_msg = '''
指令说明:-acc [t] [单曲acc值]

t为查询的段位(*dan|*danv2|rf*)[*换成对应的数字或字母] 下面是例子:
-acc 2dan 99.26-98.63-97.32-96.11
'''
help = on_command("acc help", aliases={'acc 帮助', })
@help.handle()
async def _(bot: Bot, event: Event):
    await help.finish(help_msg, at_sender=True)

malody = on_command('acc')
@malody.handle()
async def _(bot: Bot, event: Event):
    msg = str(event.get_message())
    msg = msg.strip()
    if msg[0] in command_start:
        msg = msg[1:]
    msg = msg.replace("acc", "").strip().split(" ")
    t = msg[0]
    accs = msg[1].split("-")
    try:
        result = calculate_acc(accs[0], accs[1], accs[2], accs[3], t)
        acc1 = str(result[0])[:5]
        acc2 = str(result[1])[:5]
        acc3 = str(result[2])[:5]
        acc4 = str(result[3])[:5]
    except Exception as e:
        await malody.finish("失败，输入参数有误或不存在", at_sender=True)
    await malody.finish("\n您的第一首acc是:{}%\n您的第二首acc是:{}%\n您的第三首acc是:{}%\n您的第四首acc是:{}%".format(acc1, acc2,
                                                                                                          acc3, acc4),
                        at_sender=True)
