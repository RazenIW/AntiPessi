#!/usr/bin/env python
# Anti Pessi By Razen s/o Tarace 667 ekip

from time import sleep
from TwitterAPI import TwitterAPI
from datetime import datetime
import random

# Tokens Twitter API --------------------

consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

# Paramètres ----------------------------

# Nombre de Pessis que vous voulez bloquer par jour (Twitter bloquera votre application si vous en bloquez trop)
limite = 90

# Chemin vers le fichier qui sert à stocker les ID des Pessi bloqués aujourd'hui
pathToBlockedToday = "/path/to/blocked_today.txt"

# Ne pas toucher ce qui suit ------------

blockedToday = sum(1 for line in open(pathToBlockedToday))

if blockedToday >= limite:
    exit()

keywords = {"pessi", "masterclass", "akhy", "akhi", "genant", "fraude", "réel", "prime", "malaise", "supprime",
            "goatesque", "finito", "pleure", "chiale", "chouine", "couine", "aboie", "miaule", "oukhty", "oukhti"}

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

blocked = set(api.request("blocks/ids", {"stringify_ids": "true"}))
tweets = api.request("search/tweets", {"q": " OR ".join(keywords) + " exclude:retweets", "count": "100", "result_type": "recent"})
users = [dict(t) for t in {tuple(d.items()) for d in list({"uid": t["user"]["id_str"], "tn": t["user"]["name"], "aro": t["user"]["screen_name"]} for t in tweets)}]
toBlock = []

for u in users:
    if u["uid"] not in blocked:
        if "pessi" in str.lower(u["tn"]) or "pessi" in str.lower(u["aro"]):
            toBlock.append(u)

inter = range(len(toBlock)) if blockedToday + len(toBlock) <= limite else range(limite - blockedToday)

if toBlock:
    for x in inter:
        sleep(random.uniform(1, 8))
        api.request("blocks/create", {"user_id": toBlock[x]["uid"]})
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "- @" + toBlock[x]["aro"], "a été bloqué.")
    with open(pathToBlockedToday, "a") as file:
        file.write(("" if blockedToday == 0 else "\n") + "\n".join(toBlock[x]["uid"] for x in inter))
