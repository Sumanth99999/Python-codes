list = [2,77,45,15,9] 
len = len(list)
for i in range(0,len):
    for j in range(i+1,len):
        if list[i]>list[j]:
            temp = list[i]
            list[i]=list[j]
            list[j]=temp
print(list[-1])
