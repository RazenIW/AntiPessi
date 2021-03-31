#!/usr/bin/env python
# Anti Pessi By Razen s/o Tarace 667 ekip

from time import sleep
from TwitterAPI import TwitterAPI
from datetime import datetime
import random
import sys

# Tokens Twitter API --------------------

consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

# Paramètres ----------------------------

# Nombre de Pessis que vous voulez bloquer par jour (Twitter bloquera votre application si vous bloquez trop de comptes par jour
limite = 90

# Le chemin vers le fichier qui sert à stocker les ID des Pessi bloqués aujourd'hui
pathToBlockedToday = "/path/to/blocked_today.txt"

# Ne pas toucher ce qui suit ------------

blockedToday = sum(1 for line in open(pathToBlockedToday))

if blockedToday >= limite:
    sys.exit()

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

keywords = {"pessi", "masterclass", "akhy", "akhi", "genant", "fraude", "réel", "prime", "malaise", "supprime",
            "delete", "goatesque", "finito", "pleure", "chiale", "chouine", "couine", "aboie", "miaule", "oukhty",
            "oukhti"}

blockedIds = list(api.request('blocks/ids'))
results = api.request("search/tweets", {"q": " OR ".join(keywords) + " exclude:retweets", "count": "100", "result_type": "recent"})
toBlock = list(dict())

for tw in results:
    uid, tn, aro = tw["user"]["id"], tw["user"]["name"], tw["user"]["screen_name"]
    if "pessi" in str.lower(tn) or "pessi" in str.lower(aro):
        if uid not in blockedIds and not any(d["uid"] == uid for d in toBlock):
            toBlock.append({"uid": str(uid), "aro": aro})

amtToBlock = range(len(toBlock)) if blockedToday + len(toBlock) <= limite else range(0, limite - blockedToday)

with open(pathToBlockedToday, "a") as file:
    file.write(("" if blockedToday == 0 else "\n") + "\n".join(toBlock[i]["uid"] for i in amtToBlock))
    for i in amtToBlock:
        sleep(random.uniform(1, 8))
        api.request("blocks/create", {"user_id": toBlock[i]["uid"]})
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "-", "@" + toBlock[i]["aro"], "a été bloqué.")
