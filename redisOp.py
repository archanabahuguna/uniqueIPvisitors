
class redisQ(object):

    """This class defines operations with redis queue which is used
    to store all remote ip addresses sniffed from requests"""

    def __init__(self, conn, qname=None):
        self.conn = conn
        if qname is None:
            qname = "redis:Q"
        self.queue = qname

    def push(self, ipaddr):
        return self.conn.lpush(self.queue,ipaddr)

    def pop(self):
        return self.conn.rpop(self.queue)


class redisHash(object):
    
    """This class defines operations with redis hash table (dictionary)
    which is used to maintain ip addresses for unique visitors"""

    def __init__(self, conn):
        self.conn = conn

    def set(self, ipaddr):
        return self.conn.setnx(ipaddr, 'Exists')

    def get(self, remoteip):
        return self.conn.get(remoteip)

