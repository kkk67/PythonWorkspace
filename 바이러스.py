#입력
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

#첫 번째 줄은 컴퓨터의 갯수 ,두 번째 줄은 연결되어 있는 컴퓨터 짝의 수 ,세 번째 줄부터는 연결된 컴퓨터 짝
#1번 컴퓨터가 감엳되었을 때 몇 대의 컴퓨터가 감염되었는지 출력

n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
 
dfs(1)
print(cnt)