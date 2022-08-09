# DFS의 인접 행렬(Adjacency Matrix) 방식

INF = 999999999 #논리적으로 정답이 될 수 없는 큰 값으로 초기화 하는 경우가 많음

graph_Matrix = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph_Matrix)

# DFS의 인접 리스트(Adjacency List) 방식

graph_List = [[] for _ in range(3)]

graph_List[0].append((1,7))
graph_List[0].append((2,5))

graph_List[1].append((0,7))

graph_List[2].append((0,5))

print(graph_List)

