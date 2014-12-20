import sys, random
import config
import redisOp

redisqueue = redisOp.redisQ(config.rconnQ)
redishash = redisOp.redisHash(config.rconnD)

if __name__ == '__main__':


    count = 25
    for x in xrange(count):
        remote_ipaddr=[]
        first_no = random.randint(0, 255) 
        second_no = random.randint(0, 255) 
        third_no = random.randint(0, 255) 
        fourth_no = random.randint(0, 255)
        remote_ipaddr.extend((first_no, second_no, third_no, fourth_no))
        print "[ "
        for i in remote_ipaddr:
            print i,
        print "]\n"

        redisqueue.push(remote_ipaddr)

