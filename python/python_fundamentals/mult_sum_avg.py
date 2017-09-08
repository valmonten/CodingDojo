# # This is odds to 1000
for x in range(0, 1000):
    if x%2 is not 0:
        print x

# # This is multiples of 5 to 1,000,000
for x in range(5,1000000):
    if x%5 is 0:
        print x

# Sums the list
a = [1, 2, 5, 10, 255, 3]
sm=0
for number in a:
    sm+=number
print sm

# Averages the list
sm=0
for number in a:
    sm+=number
print "average is ", sm/len(a)
