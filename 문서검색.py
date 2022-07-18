doc = input()
key = input()
cnt = 0
n = 0
while n <= len(doc) - len(key):
    if doc[n:n + len(key)] == key:
        cnt += 1
        n += len(key)
    else:
        n += 1
print(cnt)









    



