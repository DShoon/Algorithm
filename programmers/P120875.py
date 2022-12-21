from itertools import combinations

def solution(dots=[[1, 4], [9, 2], [3, 8], [11, 6]]):
    # dots = 점 네 개의 좌표를 다음 이차원 배열, 좌표평면 위의 점
    # 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1, 없으면 0
    
    # dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
    # dots = [[3, 5], [4, 1], [2, 4], [5, 10]]
    
    diffs = []
    
    for (x1, y1), (x2, y2) in combinations(dots, 2):
        diffs.append((y2-y1, x2-x1))
    
    for (x1, y1), (x2, y2) in combinations(diffs, 2):
        if x1*y2==x2*y1:
            return 1
    
    return 0
    

if __name__ == "__main__":
    result = solution()
    print(result)

