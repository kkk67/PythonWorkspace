import re


n,m,k=map(int,input().split())
array=list(map(int,input().split()))
array.sort(reverse=True)

max_value = array[0]
second_value= array[1]

result=0

while True:
    for i in range(k):
        if m==0:
            break
        result += max_value
        m -= 1
    if m==0:
        break
    result += second_value
    m-=1

print(result)
    




