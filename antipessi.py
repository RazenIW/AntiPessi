# Anti Pessi By Razen s/o Tarace 667 ekip

from time import sleep
from TwitterAPI import TwitterAPI
from datetime import datetime
import random

# API Tokens

consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

# Instanciation API

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# Vocabulaire Pessi

keywords = {"pessi", "masterclass", "akhy", "akhi", "genant", "fraude", "réel", "prime", "malaise", "supprime",
            "delete", "goatesque", "finito", "pleure", "chiale", "chouine", "couine", "aboie", "miaule", "oukhty",
            "oukhti"}

# Récupération liste des profils bloqués, et des tweets cancer

blockedUsers = list(api.request('blocks/ids'))
results = api.request("search/tweets", {"q": " OR ".join(keywords) + " exclude:retweets", "count": "100", "result_type": "recent"})

# Si le tn ou le @ du mec contient "pessi" alors on le bloque ce fdp

for tw in results:
    rand, uid, tn, aro = random.uniform(1, 5), tw["user"]["id"], tw["user"]["name"], tw["user"]["screen_name"]
    if "pessi" in str.lower(tn) or "pessi" in str.lower(aro):
        if uid not in blockedUsers:
            sleep(rand)
            api.request("blocks/create", {"user_id": uid})
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "-", "@" + aro, "a été bloqué.")
            blockedUsers.append(uid)
