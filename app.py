import sys, random
import config
import redisOp

if __name__ == '__main__':

    for x in xrange(count):
        first_no = random.randint(0, 255) 
        second_no = random.randint(0, 255) 
        third_no = random.randint(0, 255) 
        fourth_no = random.randint(0, 255)
        remote_ipaddr.append(first_no, second_no, third_no, fourth_no)

    redisQ = redisQ(rconnQ)
    redisH = redisHash(rconnD)
