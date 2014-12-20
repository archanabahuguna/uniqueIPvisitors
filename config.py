import redis

#Connection handle to redis server for Redis queue for dumping all IPs
QPOOL = redis.ConnectionPool(host='192.168.33.10', port=6379, db=0)
rconnQ = redis.Redis(connection_pool=QPOOL)

#Connection handle to redis server for Redis hash that maintains unique IPs
HPOOL = redis.ConnectionPool(host='192.168.33.10', port=6379, db=0)
rconnD = redis.Redis(connection_pool=HPOOL)
