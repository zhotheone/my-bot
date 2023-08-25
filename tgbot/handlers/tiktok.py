from tiktok_downloader import snaptik
from aiogram import Dispatcher, types
from aiogram import filters
from aiogram.types import InputFile
import random
import string
import os


async def tiktok(message: types.Message):
    name = ''.join(random.choice(string.ascii_lowercase) for i in range(4)) + '.mp4'
    vid=snaptik(f'{message.text}')
    vid[0].download(name)
    to_send = InputFile(name)
    await message.reply_video(to_send, caption='downloaded from tiktok by @zhotheonebot')
    os.remove(name)


def register_tiktok(dp: Dispatcher):
    dp.register_message_handler(tiktok, filters.Text(contains='tiktok'))