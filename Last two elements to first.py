a = [33,2,1,4,12,44,6,98]
b = len(a)
for i in range(0,b):
    for j in range(i+1,b):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
print(a[:-3])
