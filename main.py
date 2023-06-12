import os
from dotenv import load_dotenv
import requests

import callback
from tipplyListener import TipplyListener

tipplyUrl = os.getenv("TIPPLY_URL")
webhookUrl = os.getenv("WEBHOOK_URL")

print("Starting event listener..")

listener = TipplyListener(tipplyUrl)
listener.startListening(callback.onCallback, callback.offCallback)

print("end")


