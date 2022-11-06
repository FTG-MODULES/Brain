
from telethon.tl.types import Message
from .. import loader, utils

@loader.tds
class МозгMod(loader.Module):
    """мозг"""

    strings = {"name": "мозг"}

    @loader.command()
    async def мозгcmd(self, message: Message):
        """<реплай + текст> - отправляет видео с мозгом по реплаю"""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        m = "https://t.me/HACKER_PHONE_VIP_CHAT/1492480"
        if reply:
            await self.client.send_file(message.chat_id, file=m, caption=f'<i> © {args}</i>', reply_to=reply)
        else:
            await message.respond(file=m)
        if message.out:
            await message.delete()
            
# meta developer: @HPV_MODULES_VIP
# 
#
# This module was created by the
# AstroModules team specifically for this
# channel.  There is no license and banner
# here, since it is not really needed
#
#                           © AstroModules 
