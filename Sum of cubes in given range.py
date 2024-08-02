a=int(input('Enter starting range: '))
b=int(input('Enter ending range: '))
sum=0
for i in range(a,b+1):
    sum=sum + i*i*i
print(sum)
