n= int(input())

hills=list(map(int,input().split()))

highest=0
tmp=0
count=0
  
for hill in hills:
  if hill > highest:
    highest= hill
    count=0
  else:
    count+=1
  tmp=max(tmp,count)

print(tmp)



