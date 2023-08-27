a, b = map(int, input().strip().split(' '))
tmpstr = ''
for i in range(0, b):
    for j in range(0, a):
        tmpstr += '*'
    tmpstr += '\n'
print(tmpstr)