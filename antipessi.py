# Anti Pessi By Razen s/o Tarace 667 ekip

from TwitterAPI import TwitterAPI

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

blockedUsers = list({'user': user['screen_name']} for user in api.request('blocks/list'))
results = api.request("search/tweets", {"q": " OR ".join(keywords), "count": "250", "result_type": "recent"})

# Si le tn ou le @ du mec contient "pessi" alors on le bloque ce fdp

for tweet in results:
    tn, aro = tweet["user"]["name"], tweet["user"]["screen_name"]
    if "pessi" in str.lower(tn) or "pessi" in str.lower(aro):
        if tweet["user"]["id"] not in blockedUsers:
            api.request("blocks/create", {"screen_name": aro})
            print(tn + " (@" + aro + ") a été bloqué.")
