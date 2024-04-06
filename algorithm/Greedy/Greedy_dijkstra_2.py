import heapq

def dijkstra(graph, start):
    # 시작 정점으로부터의 최단 거리를 저장할 딕셔너리
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  
    # 최단 거리가 확정된 정점들의 집합
    visited = set()  
    # 최단 거리를 갱신할 수 있는 간선들을 저장할 우선순위 큐
    queue = [(0, start)]   
    while queue:
        # 현재 정점까지의 최단 거리와 정점을 가져옴
        current_distance, current_vertex = heapq.heappop(queue)
        
        # 이미 방문한 정점이면 스킵
        if current_vertex in visited:
            continue
        
        # 현재 정점을 방문한 것으로 표시
        visited.add(current_vertex)
        
        # 현재 정점과 연결된 정점들을 순회하며 최단 거리를 업데이트
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            # 현재 정점을 통해 다른 정점으로 가는 거리가 더 짧으면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# 예제 그래프
graph = {
    '1': [('2',20), ('4', 10)],
    '2': [('1', 20), ('3', 30), ('4', 20)],
    '3': [('2', 30), ('6', 50)],
    '4': [('1', 10), ('2', 20), ('5', 10)],
    '5': [('4', 10), ('6', 20)],
    '6': [('3', 50), ('5', 20)],
}

# 시작 정점
start_vertex = '1'
# 도착 정점
end_vertex = '6'


shorts = dijkstra(graph, start_vertex)# 다익스트라 알고리즘 수행
short= shorts[end_vertex] # 도착 정점까지의 최단 거리와 경로
# 결과 출력
print(f"{start_vertex}에서 {end_vertex}까지의 최단 거리: {short}")

# 경로 출력
current_vertex = end_vertex
path = [current_vertex]
while current_vertex != start_vertex:
    for neighbor, weight in graph[current_vertex]:
        if shorts[current_vertex] == shorts[neighbor] + weight:
            path.append(neighbor)
            current_vertex = neighbor
            break
path.reverse()
