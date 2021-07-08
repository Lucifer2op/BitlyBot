#@mrlokaman 
#@lntechnical
from pyrogram import Client, filters
import requests 
import json 
import os

TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID",12345))
API_HASH = os.environ.get("API_HASH","")
ADRINO_TOKEN = os.environ.get("ADRINO_TOKEN","")

headers = {
    'Authorization': ADRINO_TOKEN,
    'Content-Type': 'application/json',
}


app = Client("pdiskbot" ,bot_token = TOKEN ,api_id = API_ID ,api_hash = API_HASH )

@app.on_message(filters.private & filters.command(['start']))
async def start(client,message):
  await message.reply_text(f"Hello {message .from_user.first_name}\nhello i am adrinolinks.in short link genrator\n made with love by @Lucifer_morning_star_op ", reply_to_message_id = message.message_id)
$long_url = urlencode('adrinolinks.in');
$api_url = "https://adrinolinks.in/api?api={$ADRINO_TOKEN}&url={$long_url}&alias=CustomAlias";
$result = @json_decode(file_get_contents($api_url),TRUE);
if($result["status"] === 'error') {
 echo $result["message"];
} else {
 echo $result["shortenedUrl"];
}
  
app.run()
