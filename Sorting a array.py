arr = [98,3,45,32,67,9,108]
n = len(arr) 
for i in range(0,n):
    for j in range(i+1, n):
        if(arr[i]>arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)
