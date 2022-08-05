n = int(input())
data = list(input())

for i in range(n-1):
    data2= list(input())
    for j in range(len(data)):
        if data[j] != data2[j]:
            data[j] = '?'

print("".join(data))


