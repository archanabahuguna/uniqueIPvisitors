import app

if __name__ == '__main__':
        #Check if this visitor visited in the given timeframe
        remoteip = [192, 168, 33, 10]
        if (app.redishash.get(remoteip)):
            print "The visitor with unique IP %d %d %d %d visited the site" % (remoteip[0], remoteip[1], remoteip[2], remoteip[3])
        else:
            print "The visitor with unique IP did not visit the site" 
