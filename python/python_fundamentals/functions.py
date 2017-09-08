def even_odds_2000():
    for x in range(0,2001):
        if x%2==1:
            print "number is "+ str(x) +". This is an odd number."
        else:
            print "number is "+ str(x) +". This is an even number."
# even_odds_2000()

def regulators(li,mult):
    for x in range(0,len(li)):
        li[x] *= mult
    print li
    return li
a=[2,4,10,16]


def hacker(lis):
    arr=[]
    for x in range(0,len(lis)):
        z=lis[x]
        arr.append([])
        for y in range(0,z+1):
            arr[x].append(1)
    print arr
hacker(regulators(a, 5))
