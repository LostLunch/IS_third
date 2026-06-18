import heapq
from math import inf
from .reconsturct_path import reconstruct_path

def heuristic(node,next_node):
    x,y,_ = node
    next_x, next_y, _ = next_node
    return abs(x - next_x) + abs(y - next_y)

def astar(graph, start, target):
    g_score = {node: inf for node in graph.nodes}   #거리를 모두 무한대로 설정
    g_score[start] = 0  #시작점은 0으로

    f_score = {node: inf for node in graph.nodes} #휴리스틱 점수 계산
    f_score[start] = heuristic(start, target) #시작점의 휴리스틱 점수 계산

    predecessors = {node: None for node in graph.nodes}  #경로 딕셔너리를
    pq = [(0.0, start)]   #우선순위 큐에 거리와 시작 지점을 저장

    while pq:
        curr_f, curr_node = heapq.heappop(pq) #현재 노드와 거리를 우선순위 큐에서 추출

        if curr_f > f_score[curr_node]: #현재 거리가 저장된 거리보다 크면 넘김
            continue
        if curr_node == target: #도착 노드에 도착하면 탐색을 끝냄
            break

        for neighbor, weight in graph.get_neighbors(curr_node): #이웃 노드와 가중치를 가져옴
            new_g = g_score[curr_node] + weight #현재 노드에서 이웃 노드까지의 거리 계산

            if new_g < g_score[neighbor]: #계산된 거리가 저장된 거리보다 작으면 업데이트
                g_score[neighbor] = new_g
                f_score[neighbor] = new_g + heuristic(neighbor, target)
                predecessors[neighbor] = curr_node #이웃 노드의 이전 노드를 현재 노드로 설정
                heapq.heappush(pq, (f_score[neighbor], neighbor)) #업데이트된 거리와 이웃 노드를 우선순위 큐에 추가
    path = reconstruct_path(predecessors, start, target) #경로 역추적 함수 호출
    
    return path, g_score[target]