str = input()
tmp = ''
for i in str:
    if i.isupper() == True:
        tmp += i.lower()
    elif i.islower() == True:
        tmp += i.upper()
print(tmp)