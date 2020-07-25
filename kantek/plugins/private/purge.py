"""Plugin to purge messages up to a specific point"""
import logging

from telethon.tl.custom import Message
from telethon.tl.types import Channel

from utils.client import KantekClient
from utils.pluginmgr import k

tlog = logging.getLogger('kantek-channel-log')


@k.command('purge')
async def puge(client: KantekClient, chat: Channel, msg: Message, event) -> None:
    """Purge all messages from the the point the command was sent to the message that was replied to.

    This command is unavailable in private for the moment since private message ids are shared across PMs

    Examples:
        {cmd}
    """
    await msg.delete()
    if event.is_private:
        return
    if not msg.is_reply:
        return
    else:
        reply_msg: Message = await msg.get_reply_message()
        await client.delete_messages(chat, list(range(reply_msg.id, msg.id)))
