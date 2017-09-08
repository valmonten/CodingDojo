me = {"name": "Anna","age":101,"country of birth": "Israel", "favorite language":"Klingon"}
def get_info(obj):
    for key in obj:
        print "My "+str(key)+" is "+str(obj[key])
get_info(me)