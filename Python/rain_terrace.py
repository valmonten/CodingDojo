def rain_terrace(arr):
    front = -1
    end = -1
    indmax = 0
    maxs = 1
    for x in range(0,len(arr)-1):
        front = x
        if arr[x] > arr[x+1]:
            break
    for y in range(len(arr)-1,0,y-=1):
        end = y
        if arr[y] > arr[y-1]:
            break
    for z in range(0,len(arr)-1):
        if arr[indmax]<arr[z]:
            indmax = z
    for alpha in range (0,len(arr)-1):
        if arr[indmax] == arr[alpha]:
            maxs +=1
    
