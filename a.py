n,m = map(int,input().split()) # n은 책의 개수 m은 상자 최대무게

if n==0:
    print(0)
else:
    l = list(map(int, input().split()))
    
    count=1
    sum=0
    for i in range(n-1,-1,-1):

        sum += l[i]
        if sum > m:
            count += 1
            sum= l[i]

    print(count)


