# Anti Pessi By Razen s/o Tarace 667 ekip

from TwitterAPI import TwitterAPI
from datetime import datetime

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

arr = []
blockedUsers = list(api.request('blocks/ids'))
results = api.request("search/tweets", {"q": " OR ".join(keywords) + " exclude:retweets", "count": "100", "result_type": "recent"})

for tw in results:
    uid, tn, aro = tw["user"]["id"], tw["user"]["screen_name"], tw["user"]["name"]
    if "pessi" in str.lower(tn) or "pessi" in str.lower(aro):
        if uid not in blockedUsers and uid not in arr:
            api.request("blocks/create", {"user_id": uid})
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - " + tn + " (@" + aro + ") a été bloqué.")
            arr.append(uid)
