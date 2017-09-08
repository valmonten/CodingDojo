import random
def ten_students_scores():
    for x in range(0,10):
        random_num = random.randint(60,100)
        if random_num < 69:
            print "Score: " + str(random_num) + "; Your grade is D"
        if random_num <= 79 and random_num > 69:
            print "Score: " + str(random_num) + "; Your grade is C"
        if random_num <= 89 and random_num > 79:
            print "Score: " + str(random_num) + "; Your grade is B"
        if random_num <= 100 and random_num > 89:
            print "Score: " + str(random_num) + "; Your grade is A"

ten_students_scores()

