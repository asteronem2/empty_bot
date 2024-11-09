import re
from typing import NoReturn

from Bot import MsgModel
from Interfaces import TextMessageInterface


class StartMsg(TextMessageInterface):
    async def define(self) -> NoReturn | dict:
        rres = re.search(r'^/start', self.text_low)
        if rres:
            return {
                'dict1': 250
            }

    async def process(self, *args, **kwargs) -> None:
        print(kwargs.get('dict1'))
        await self.bot.send_message(MsgModel(
            chat_id=self.chat.id,
            text=self.locale['StartMsg']
        ))