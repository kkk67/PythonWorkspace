s = list(map(int,input()))
count=0
prev = '?'

for i in s:
    if i !=prev:
        prev = i
        count += 1

print((count//2))
