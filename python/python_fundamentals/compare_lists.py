def compare_lists(li1,li2):
    if len(li1)!=len(li2):
        print "Not identical1"
        return
    for x in range(0,len(li1)):
        if li1[x]!=li2[x]:
            print "Not identical2"
            return
    print "Identical!"
list_one = [1,2,5,6,2,4]
list_two = [1,2,5,6,2,3]
compare_lists(list_one,list_two)

    