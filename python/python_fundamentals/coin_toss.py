import random
def coin_toss_5000():
    print "Starting Program FLIPOMATIC 5000!!!"
    tails=0
    heads=0
    for x in range(1,5001):
        randomizer = random.randint(1,2)
        if randomizer == 1:
            heads+=1
            print "Attempt #" +str(x)+": Throwing a coin... It's a head!... Got " +str(heads)+"head(s) so far and " +str(tails)+ "tail(s) so far"
        if randomizer == 2:
            tails+=1
            print "Attempt #" +str(x)+": Throwing a coin... It's a tail!... Got " +str(heads)+"head(s) so far and " +str(tails)+ "tail(s) so far"
coin_toss_5000()