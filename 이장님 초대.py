n = int(input())

long = list(map(int,input().split()))
long.sort(reverse=True)

for i in range(len(long)):
    long[i] = long[i] + i + 1


print(max(long) + 1)


