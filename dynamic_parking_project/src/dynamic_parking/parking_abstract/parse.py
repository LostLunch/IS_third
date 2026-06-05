def parse_txt(file_path: str) -> list[list[int]]: # 텍스트 파일을 2차원 배열화
    map = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split() # 문자열로 읽은 숫자를 정수로 변환
            for i in range(len(data)):
                match data[i]:
                    case 'S':
                        data[i] = '0' # 통로는 0으로 표현
                    case 'W':
                        data[i] = '1' # 벽은 1으로 표현
                    case 'P':
                        data[i] = '2' # 주차 공간은 2으로 표현
                    case 'D':
                        data[i] = '3' # 주차 방향은 3으로 표현
                    case _:
                        pass
            data = [int(item) for item in data]
            map.append(data)
    return map

