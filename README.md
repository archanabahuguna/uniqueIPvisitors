uniqueIPvisitors
================

Code for keeping a count for no of unique visitors to a website within a given timeframe.

Design: (Not final) A module (say app.py) provides IP addresses for every request within a given timeframe. A Redis queue is used to store these IPs temporarily and a Redis dictinoary is used to store unique IP addresses. The app.py module pushes all IPs from requests to Redis Queue, while workers pop the IPs and push to Redis dict unique IPs (the uniqueness is taken care of by the hashing operation of redis dict itself and the setnx operation)

Files:
app.py- 
        gets/generates input IP addresses
        Uses redis client to push IPs into a queue within given timeframe
        Will implement sharding to take care of ip load for multiple qs

redisOp.py- 
        defines classes for operating on a redis queue and a dictionary
        Will implement multiple queues

config.py-
        configuration for redis

worker.py-
        pops ip addresses from redis queue and pushes into redis dictionary        ip addresses are pushed in dictionary only if unique
        May implement logging of unique Ips for file logging option in case        info on all unique ips is needed

admin.py-
        checks if given IP has visited the website in the given timeframe
        May also get list of all IPs from file (logged by worker) if needed
