x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def counting_stars(li):
    for numb in li:
        if isinstance(numb, int):
            print numb*"*"
        if isinstance(numb, str):
            print numb[0].lower()*len(numb)
counting_stars(x)