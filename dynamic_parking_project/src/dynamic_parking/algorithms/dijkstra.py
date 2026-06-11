import heapq
from math import inf
from .reconsturct_path import reconstruct_path

def dijkstra(graph, start, target):
    distances = {node: inf for node in graph.nodes}   #거리를 모두 무한대로 설정
    distances[start] = 0  #시작점은 0으로
    predecessors = {node: None for node in graph.nodes}  #경로 딕셔너리를
    pq = [(0, start)]   #우선순위 큐에 거리와 시작 지점을 저장

    while pq:
        curr_dist, curr_node = heapq.heappop(pq) #현재 노드와 거리를 우선순위 큐에서 추출

        if curr_dist > distances[curr_node]: #현재거리가 저장된 거리보다 크면 넘김
            continue
        if curr_node == target: #도착 노드에 도착하면 탐색을 끝냄
            break

        for neighbor, weight in graph.get_neighbors(curr_node): #이웃 노드와 가중치를 가져옴
            distance = curr_dist + weight #현재 노드에서 이웃 노드까지의 거리 계산

            if distance < distances[neighbor]: #계산된 거리가 저장된 거리보다 작으면 업데이트
                distances[neighbor] = distance
                predecessors[neighbor] = curr_node #이웃 노드의 이전 노드를 현재 노드로 설정
                heapq.heappush(pq, (distance, neighbor)) #업데이트된 거리와 이웃 노드를 우선순위 큐에 추가

        path = reconstruct_path(predecessors, start, target) #경로 역추적 함수 호출
    return path, distances[target]