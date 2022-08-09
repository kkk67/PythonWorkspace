n = int(input())
list = []
array = []
for i in range(n):
    list.append(int(input()))
list.sort(reverse=True)

for j in range(n):
    array.append(list[j]* (j+1))

print(max(array))


