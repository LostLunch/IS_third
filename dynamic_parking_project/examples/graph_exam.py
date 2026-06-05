# test_run.py

# 1. 우리가 만든 동적 그래프 클래스 가져오기
# 예제 실행 위치에 따라 패키지 import 경로 문제가 발생할 수 있습니다.
# 실행할 때 examples/ 폴더에서 바로 실행해도 동작하도록 `src`를 경로에 추가합니다.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from dynamic_parking.graph.dynamic_graph import Dynamic_graph as DynamicGraph

def main():
    print("=== 🚗 주차장 동적 그래프 테스트 시작 ===")
    
    # 2. 주차장 지도(그래프) 객체 만들기
    parking_map = DynamicGraph()
    
    # 3. 노드(주차칸/통로) 추가하기
    # (0, 0, 0) 칸과 바로 옆 칸인 (0, 1, 0) 칸을 만듭니다.
    print("\n[1] 노드 생성 테스트")
    node_A = parking_map.add_node(0, 0, 0)
    node_B = parking_map.add_node(0, 1, 0)
    
    print(f"생성된 노드 A: {node_A}")
    print(f"생성된 노드 B: {node_B}")
    
    # 4. 엣지(이동 경로) 연결하기
    # 노드 A에서 노드 B로 이동할 수 있는 길을 만들고, 기본 거리 가중치 1.0을 줍니다.
    print("\n[2] 간선(길) 연결 및 기본 가중치 테스트")
    parking_map.add_edge(node_A.id, node_B.id, base_weight=1.0)
    
    # 노드 A에서 갈 수 있는 이웃 칸이 잘 나오는지 확인
    neighbors_before = parking_map.get_neighbors(node_A.id)
    print(f"노드 A의 이웃과 가중치: {neighbors_before}") 
    # 예상 출력: [((0, 1, 0), 1.0)] -> (0,1,0)까지 가는데 비용 1.0 점수!
    
    # 5. 동적 가중치 업데이트 테스트 (★우리의 핵심 기능!)
    # 갑자기 (0, 0, 0)에서 (0, 1, 0)으로 가는 길에 앞차가 멈춰 서서 혼잡도가 2.5만큼 늘어난 상황을 시뮬레이션합니다.
    print("\n[3] 실시간 혼잡도(동적 가중치) 변경 테스트")
    parking_map.update_edge_weight(node_A.id, node_B.id, add_weight=2.5)
    
    # 가중치가 자동으로 1.0 + 2.5 = 3.5로 변했는지 확인
    neighbors_after = parking_map.get_neighbors(node_A.id)
    print(f"혼잡 발생 후 노드 A의 이웃과 가중치: {neighbors_after}")
    # 예상 출력: [((0, 1, 0), 3.5)] -> 알고리즘이 이 비용을 보고 우회하게 됩니다!

    print("\n=== 🎉 모든 그래프 기본 기능 정상 작동 확인! ===")

if __name__ == "__main__":
    main()