import app

if __name__ == '__main__':
    while (1):
        #get remote up address from redis list
        remoteip = app.redisqueue.pop()
        if remoteip:
            #Set Ip Address in Redis hash table - unique IP 
            if app.redishash.set(remoteip):
                print "Remote Ip is unique, added to Redis dictionary"
        #can also keep list of IPs in memory and dump into file JSOn format
        #every t interval so we can have a file with all IPs as well
