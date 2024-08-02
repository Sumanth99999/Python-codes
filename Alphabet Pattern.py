# Printing Pattern in Ascending Order

def aplhabet_pattern():
    a = int(input('starting number:'))
    for i in range(0,a+1):
        for j in range(65,65+i):
            print(chr(j), end =" ")
        print()

aplhabet_pattern()


# Reverse in Descending order

def aplhabet_pattern():
    a = int(input('starting number:'))
    for i in range(a,0,-1):
        for j in range(65,65+i):
            print(chr(j), end =" ")
        print()

aplhabet_pattern()

