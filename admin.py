if __name__ == '__main__':
        #Check if this visitor visited in the given timeframe
        remoteip = [192, 168, 33, 10]
        if (redishash.get(remoteip)):
            print "The visitor with unique IP %d visited the site" % remoteip
        else:
            print "The visitor with unique IP %d did not visit the site" % remoteip
