b,c,d = map(int,input().split())

burgur = list(map(int,input().split()))
side = list(map(int,input().split()))
drink = list(map(int,input().split()))

burgur.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

print(burgur)
print(side)
print(drink)

e = int(min(len(burgur),len(side),len(drink)))

result = sum(burgur+side+drink)
result2= int(sum(burgur[:e]+side[:e]+drink[:e])*0.9 + sum(burgur[e:] +side[e:]+drink[e:]) )

print(result)
print(result2)
