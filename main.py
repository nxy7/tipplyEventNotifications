from dotenv import load_dotenv
load_dotenv()

import os
import requests

import callback
import time
from tipplyListener import TipplyListener

tipplyUrl = os.getenv("TIPPLY_URL")

print("Starting event listener..")

listener = TipplyListener(tipplyUrl)
listener.startListening(callback.onCallback, callback.offCallback)

print("end")


