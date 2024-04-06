import heapq
def prim(graph):
    
    num_vertices = len(graph) # 그래프의 정점 개수 
   
    visited = set() # 방문한 정점을 저장하는 set
    
    mst = []# 최소 신장 트리의 간선 리스트
    
    # 임의의 시작 정점을 선택
    start_vertex = list(graph.keys())[0]
    
    
    visited.add(start_vertex) # 시작 정점을 방문으로 기록
    
    # 시작 정점과 연결된 간선을 우선순위 큐에 추가
    edges = [(cost, start_vertex, neighbor) for neighbor, cost in graph[start_vertex]]
    heapq.heapify(edges)
    
    while edges:
        # 최소 비용의 간선을 가져옴
        cost, src, dest = heapq.heappop(edges)
        # 이미 방문한 정점이면 다음 간선 확인
        if dest in visited:
            continue

        # 최소 신장 트리에 간선 추가
        mst.append((src, dest, cost))
        visited.add(dest)# 방문으로 기록
    
        # 새로 추가된 정점과 연결된 간선을 우선순위 큐에 추가
        for neighbor, cost in graph[dest]:
            if neighbor not in visited:
                heapq.heappush(edges, (cost, dest, neighbor))
    
    return mst

graph = {
    'A': [('B', 2), ('C', 3),('E', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 1), ('C', 2),('E', 2)],
    'E': [('A', 3), ('D',2)]
}

mst = prim(graph) #prim 실행

print("최소 신장 트리")
for edge in mst:
    print(edge)
