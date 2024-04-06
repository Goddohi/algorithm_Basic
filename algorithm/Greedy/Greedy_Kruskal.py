def kruskal(graph):
    parent = {}  # 각 노드의 부모 노드를 저장할 딕셔너리
    rank = {}    # 각 노드의 랭크를 저장할 딕셔너리
    mst = []     # 최소 신장 트리를 저장할 리스트

    #루트노드 찾는함수
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2): # 두 노드를 하나로 합치는 함수
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1] += 1

    # 각 노드를 자기 자신의 부모로 초기화
    for v in graph:
        parent[v] = v
        rank[v] = 0

    #모든간선을 넣고 정렬
    edges = [] 
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            edges.append((node, neighbor, weight))
    edges.sort(key=lambda x: x[2])
    
    #순회하면서 루트노드가 다르면 다른트리로 인식후 합침
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))

    return mst

# 주어진 그래프
graph = {
    'A': [('B', 2), ('C', 3),('E', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 1), ('C', 2),('E', 2)],
    'E': [('A', 3), ('D',2)]
}

# 크루스칼 알고리즘 적용 및 결과 출력
mst = kruskal(graph)
print("최소 신장 트리:")
for edge in mst:
    print(edge)
