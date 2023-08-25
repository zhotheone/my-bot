import os
import subprocess
from aiogram import Dispatcher, types
from aiogram import filters
from aiogram.types import InputFile

async def instagram(message: types.Message):
    shortcode = message.text.split(sep='/')[-2]
    print(shortcode)
    subprocess.run([f'instaloader', '--no-metadata-json', '--filename-pattern', '{target}', '--', f'-{shortcode}'])
    cwd = os.getcwd()
    os.chdir(f'-{shortcode}')
    f = open(f'-{shortcode}.txt', 'r', encoding='UTF-8')
    text = f.read()
    f.close()
    if os.path.isfile(f'-{shortcode}.mp4'):
        vid = InputFile(f'-{shortcode}.mp4')
        await message.reply_video(vid, caption=f'{text}\n\ndownloaded from instagram by @zhotheonebot')
    else:
        pic = InputFile(f'-{shortcode}.jpg')
        await message.reply_photo(pic, caption=f'{text}\n\ndownloaded from instagram by @zhotheonebot')
    for file in os.listdir():
        os.remove(file)
    os.chdir(cwd)
    os.rmdir(f'-{shortcode}')

def register_instagram(dp: Dispatcher):
    dp.register_message_handler(instagram, filters.Text(contains='insta'))