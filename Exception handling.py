a = int(input('Enter a number: '))
b= int(input('Enter a number: '))
try:
    c=a/b
    print(c)
except Exception:
    print('You cannot divide a number by 0')
finally:
    print('please try again')
