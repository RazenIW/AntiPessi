# Anti Pessi pour Twitter
Programme qui bloque automatiquement les Pessi sur Twitter

Pessis que j'ai bloqué au total : [https://razen.wtf/pessis/](https://razen.wtf/pessis/)

## Pré-requis

* Tokens d'accès à [l'API Twitter](https://developer.twitter.com/en/portal/dashboard)
* Python 3.8
* [TwitterAPI](https://github.com/geduldig/TwitterAPI) 

## Utilisation

Je vous recommande d'utiliser ce script sur un [serveur Linux](https://www.digitalocean.com/products/droplets/), sur lequel vous paramétrez deux [Cron Jobs](https://cron-job.org/fr/) comme ceci :

```
*/30 * * * * python3 /chemin/vers/antipessi.py
0 0 * * * > /chemin/vers/blocked_today.txt
```

On exécute le script automatiquement toutes les 30 minutes, et on clear le fichier des Pessis bloqués tous les jours à minuit.

La raison pour laquelle on limite le nombre de blocks par jour est que Twitter bloquera votre application si vous bloquez trop de comptes par jour.

D'ailleurs, à chaque exécution je ne bloque pas tous les comptes d'un coup, il y a un délai aléatoire entre chaque traitement.

## Captures

![Bloqués](https://razen.wtf/uploads/chrome_0FandDkmyM.png)
![Logs](https://razen.wtf/uploads/pycharm64_CDDEbcfqt1.png)
