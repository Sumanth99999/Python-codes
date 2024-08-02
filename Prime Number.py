def is_prime():
    a = int(input('Enter a Number:'))
    if a == 1:
        print(a, "is not a prime number")
    if a > 1:
        
        for i in range(2,a):
            if a%i==0:
                print(a, "is not a prime number")
                break
            
            else:
                print(a,'is a prime number')

is_prime()


