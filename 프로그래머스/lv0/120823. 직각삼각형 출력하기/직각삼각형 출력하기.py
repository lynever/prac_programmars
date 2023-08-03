n = int(input())
tmp = ''
for i in range(1, n + 1):
    for j in range(i):
        tmp += '*'
    tmp += '\n'
print(tmp)