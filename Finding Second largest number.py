arr = [9,3,5,10,22,89,90]
c = len(arr)
for i in range(0,c):
    for j in range(i+1,c):
        if(arr[i]>arr[j]):
            temp = arr[i]
            arr[i]= arr[j]
            arr[j]= temp
print(arr[-2])
