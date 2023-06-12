import requests
import os


webhookUrl = os.getenv("WEBHOOK_URL")


def onCallback():
    url = webhookUrl+"/on"
    try:
        requests.get(url)
    except:
        print("")
    finally:
        print("on")


def offCallback():
    url = webhookUrl+"/off"
    try:
        requests.get(url)
    except:
        print("")
    finally:
        print("off")
