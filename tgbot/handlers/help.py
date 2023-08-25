from aiogram import Dispatcher, types
from aiogram import filters
from aiogram.utils.markdown import hcode, hbold, hitalic

async def help_com(message: types.Message):
    await message.reply(f'Tiktok: просто ссілка на видик; {hbold("КАРТИНКИ НЕ РАБОТАЮТ")}\n\nInstagram: ссілка на пост (видео, фото)\n\nSpotify:\nпринимаю просто ссілку на альбом/плейлист/трек, или ищу через \n\n{hitalic("[Найти, знайти, find] название")}\n\nC помощью ключей, можно искать альбомі, собрать все говно с исполнителя, найти публічній плейлист =>\nПримері:\n\n{hcode("найти fein")}\n{hcode("найти album: utopia")}\n{hcode("найти artist: travis scott")}\n{hcode("найти playlist: travis scott bangers")}\n{hcode("найти artist: travis scott album: utopia")}\n{hcode("найти playlist: everything artist: ariana grande")}')
def register_help(dp: Dispatcher):
    dp.register_message_handler(help_com, commands=['help'])