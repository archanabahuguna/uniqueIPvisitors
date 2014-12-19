from redis import Redis

#Connection handle to redis server for Redis queue for dumping all IPs
rconnQ = redis.Redis('192.0.33.10',6379)

#Connection handle to redis server for Redis hash that maintains unique IPs
rconnH = redis.Redis('192.0.33.10',6379)
