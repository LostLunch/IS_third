def parse_txt(file_path: str) -> tuple[list[list[int]], list[tuple[int, int, int]]]: # 텍스트 파일을 2차원 배열화
    map = []
    car_pos = []
    with open(file_path, 'r') as file:
        for y,line in enumerate(file):
            data = line.strip().split() # 문자열로 읽은 숫자를 정수로 변환
            for i in range(len(data)):
                match data[i]:
                    case 'S':
                        data[i] = '0' # 통로는 0으로 표현
                    case 'W':
                        data[i] = '1' # 벽은 1으로 표현
                    case 'P':
                        data[i] = '2' # 주차 공간은 2으로 표현
                    case 'C':
                        car_pos.append((i,y,0)) # 통로 위 차 위치는 별도로 저장
                        data[i] = '0' # 차 위치는 0으로 표현
                    case _:
                        data[i] = '1' # 그 외는 모두 벽으로 처리
            data = [int(item) for item in data]
            map.append(data)
    return map, car_pos
