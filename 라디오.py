a,b=map(int,input().split())
n = int(input())
list = []

for i in range(n):
    list.append(int(input()))
list.sort(reverse=True)

sum1= abs(b-a)

for i in range(n):
    list[i]=abs(b-list[i])
sum2= min(list)

print(min(sum1,sum2+1))







    

    