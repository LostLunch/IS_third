from __future__ import annotations
from typing import Tuple


class Node:
    def __init__(self, x : int, y: int, z : int = 0): #3차원이지만 z를 0으로 설정해 2차원 시작 -> 나중에 확장장
        self.x = x
        self.y = y
        self.z = z
        self.id : Tuple[int,int,int] = (x,y,z)
    
    def __repr__(self) -> str:  #print접근 시 출력되는 내용
        return f"Node{self.id}"

    def __eq__(self, ohter):
        if not isinstance(ohter, Node): #같은지 아닌지 판단했을 때 답 출력
            return False
        return self.id == ohter.id

    def __hash__(self): #식별표
        return hash(self.id)