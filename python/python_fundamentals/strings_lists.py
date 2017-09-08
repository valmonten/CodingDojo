words= "It's thanksgiving day! It's my birthday, too!"
print words.find("day")
print words.replace("day" , "month")

x= [2, 54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]
new_li =[]
new_li+=[x[0], x[len(x)-1]]
print new_li

k = [19,2,54,-2,7,12,98,32,10,-3,6]
k.sort()
j= [[]]
print k
for thingy in range(0, len(k)/2):
    j[0].append(k[thingy])
    # print thingy
    # k.pop(thingy-1)
for thingy in range(len(k)/2, len(k)):
    j.append(k[thingy])

# k.insert(0,j)
print j