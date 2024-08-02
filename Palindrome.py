str = input("Enter the string")
revstr = ""
for i in str:
    revstr = i+revstr
print('Reverse of string',revstr)
if str == revstr:
    print('Given string is palindrome')
else:
    print('Given string is not a palindrome')
