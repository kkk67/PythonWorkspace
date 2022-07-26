n,snake=map(int,input().split())

fruit = list(map(int,input().split()))
fruit.sort()

for i in range(len(fruit)):
    if fruit[i] <= snake:
        snake +=1
    else:
        continue

print(snake)