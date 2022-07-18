n = int(input())
score = list(map(int,input().split()))

max_val=max(score)

for i in range(n):
    score[i] = score[i] / max_val *100
    
avg_score=sum(score) / n
print(round(avg_score,6))


