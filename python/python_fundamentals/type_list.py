def list_type(li):
    count = 0
    sm = 0
    bootsandcats = "How to beat box: "

    if all(isinstance(x, int) for x in li):
        print "Type is int"
        for x in li:
            sm += x
        print sm
    elif all(isinstance(x, str) for x in li):
        print "Type is string"
        for x in li:
            bootsandcats += x
        print bootsandcats    
    else:
        print "The list is mixed"
        for x in li:
            if isinstance(x, int):
                sm+=x
            if isinstance(x, str):
                bootsandcats+=x
        print sm
        print bootsandcats


list_type(["stay", 'put', 'on', 'the', 'ground',9, 1])
