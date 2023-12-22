from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("26371250"))
API_HASH = input("a545f4b8a3a90a5039ee756807b99234")


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
