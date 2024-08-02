list = [4,4,7,8,8]
uniq=[]
dup=[]
for i in list:
    if i not in uniq:
        uniq.append(i)
    elif i not in dup:
        dup.append(i)
print(uniq)
print(dup)
