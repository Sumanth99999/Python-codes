def pattern():
    a = int(input('Enter Starting Range:'))
    b = int(input('Enter Starting Range:'))
    for i in range(a,b):
        for j in range(i+1, j+1):
            print(i,j)

    print()
pattern()
