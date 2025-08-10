from aiogram import Bot, Dispatcher 
from datetime import datetime
from aiogram.types import Message
from core import cacheloader, parcer

from aiogram.filters import CommandStart,Command



class RssBot:
    def __init__(self,token,id_channel):
        self.token = token
        self.id_channel = id_channel
        self.bot = Bot(self.token)
        self.dp = Dispatcher()
        self.rss_parsing = parcer.Parcer()
        
        


    async def _start(self,message:Message) -> None:
        await message.answer(f"Hi {message.from_user.username},\n I,m Rss news bot from channel")
    async def _spam_blyat(self):
        pass
    


    async def run(self):
        print(f"[{datetime.now}] - bot started")
        self.dp.message.register(self._start,Command('start','help'))

        await self.dp.start_polling(self.bot)

