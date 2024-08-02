str = 'hello'
uniq = " "
dup = " "
for i in str:
    if i not in uniq:
        uniq=uniq+i
    elif i not in dup:
        dup=dup+i
print('Unique Elements are', uniq)
print('Duplicate Elements are',dup)
