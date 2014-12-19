
if __name__ == '__main__':
    while (1):
        #get remote up address from redis list
        remoteip = redisQ.pop()
        #set remote ip in redis hash if unique
        if redisH.set(remoteip):
            print "Remote Ip is unique, added to Redis dictionary"
