def square():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
top=square()
for i in top:
    print(i)
        
