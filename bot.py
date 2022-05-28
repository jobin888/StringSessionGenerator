import os

from pyrogram import Client

s1 = "YOUR SESSION STRING"

app = Client(s1,  api_id=YOU_API_ID, api_hash="YOU API HASH")

app.storage.SESSION_STRING_FORMAT=">B?256sQ?"

app.start()
