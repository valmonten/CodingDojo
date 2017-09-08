name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    if arr2 > arr1:
        ky = arr2
        vl = arr1
    else:
        ky = arr1
        vl = arr2
    for x in range(0,len(ky)):
        new_dict[ky[x]]=vl[x]

    print new_dict
    return new_dict
make_dict(name,favorite_animal)
