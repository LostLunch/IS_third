# test_run.py

from dynamic_parking.parking_abstract.parse import parse_txt
from dynamic_parking.parking_abstract.grid import ParkingGrid
from dynamic_parking.parking_abstract.converter import convert_grid_to_graph

def main():
    print("=" * 50)
    print("🚗 [1단계] map.txt 파일 읽기 시작")
    print("=" * 50)
    
    # 1. 텍스트 파일을 읽어 2차원 숫자 리스트로 변환
    matrix = parse_txt("map.txt")
    print("변환된 2차원 배열:")
    for row in matrix:
        print(row)
        
    # 2. ParkingGrid 객체 생성
    grid = ParkingGrid(matrix)
    print(f"\n주차장 크기: 가로 {grid.width}칸, 세로 {grid.height}칸")

    print("\n" + "=" * 50)
    print("🔄 [2단계] 컨버터를 통해 내비게이션 지도(Graph)로 탈바꿈")
    print("=" * 50)
    
    # 3. 진짜 지도(Graph)로 변환
    graph = convert_grid_to_graph(grid)
    print("✅ 그래프 변환 성공!")

    print("\n" + "=" * 50)
    print("🔎 [3단계] 우리가 세운 주차장 물리 법칙 최종 검증")
    print("=" * 50)

    # 검증용 좌푯값 설정 (x, y, z)
    parking_space = (0, 1, 0)  # 맨 왼쪽 주차 공간 (2)
    entry_road = (1, 1, 0)     # 그 옆 주차 진입로 (3)
    normal_road = (2, 1, 0)    # 가운데 일반 도로 (0)

    # 규칙 1: 주차 공간(2)은 오직 진입로(3)하고만 연결되어야 함
    # graph.nodes[좌표].edges에 연결된 이웃 노드들의 ID가 들어있습니다.
    parking_neighbors = [edge.to_node_id for edge in graph.nodes[parking_space].edges]
    print(f"1. 주차 공간 {parking_space}에 연결된 이웃들: {parking_neighbors}")
    print(f"   -> 진입로 {entry_road}만 존재하나요? {entry_road in parking_neighbors and len(parking_neighbors) == 1}")

    # 규칙 2: 일반 도로(0)는 옆에 주차 공간(2)이 있어도 절대 바로 연결되면 안 됨
    # (이번 지도에서는 일반 도로 좌우가 다 3이라서 3들하고만 연결되어야 함)
    normal_neighbors = [edge.to_node_id for edge in graph.nodes[normal_road].edges]
    print(f"\n2. 일반 도로 {normal_road}에 연결된 이웃들: {normal_neighbors}")
    print(f"   -> 주차 공간(2)인 {parking_space}가 목록에 없나요? {parking_space not in normal_neighbors}")

    # 규칙 3: 진입로(3)는 벽이 아닌 주변 모든 길(0, 2, 3)과 자유롭게 연결되어야 함
    entry_neighbors = [edge.to_node_id for edge in graph.nodes[entry_road].edges]
    print(f"\n3. 진입로 {entry_road}에 연결된 이웃들: {entry_neighbors}")
    print(f"   -> 주차 공간(0,1,0)과 일반 도로(2,1,0)가 다 들어있나요? {parking_space in entry_neighbors and normal_road in entry_neighbors}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()