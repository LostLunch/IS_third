def reconstruct_path(predecessors,start,target):
    # 경로 역추적
    path = []
    curr = target
    while curr is not None: #목표한 노드가 시작노드가 아닌 상황에서
      path.append(curr)  #목적지부터 역순으로 리스트에 저장
      curr = predecessors[curr] #predecessors 형태 예시 : predecessors = {"A" : None, "B" : "A"}
    path.reverse()       #시작노드는 value 값으로 None을 가지고 보통의 노드는 vlaue 값으로 이전 노드를 가짐
    #마지막에 리스트를 역전시켜 원래 경로로 전환

    return path if path and path[0] == start else [] #시작이 Start인지 확인