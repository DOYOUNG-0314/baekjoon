import sys
input = sys.stdin.readline

N = int(input())

# 종이 정보 입력받기: N x N 배열 (0: 흰색, 1: 파란색)
paper = [list(map(int, input().split())) for _ in range(N)]

# 색종이 개수 저장용 변수
white = 0  # 흰색 색종이 수
blue = 0   # 파란색 색종이 수

# 정사각형 (x, y) 위치에서 시작해서 size 크기의 종이를 검사
def divide(x, y, size):
    global white, blue  # 전역 변수로 색종이 개수 증가시키기

    # 기준이 되는 색
    color = paper[x][y]
    same = True  # 이 영역이 전부 같은 색인지 체크

    # 현재 영역 전체를 검사
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                same = False  # 하나라도 다르면 나눠야 함
                break
        if not same:
            break

    if same:
        # 모두 같은 색이면 색종이로 인정
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        # 다른 색이 섞여 있으면 4등분해서 재귀 호출
        half = size // 2
        divide(x, y, half)  # 왼쪽 위
        divide(x, y + half, half)  # 오른쪽 위
        divide(x + half, y, half)  # 왼쪽 아래
        divide(x + half, y + half, half)  # 오른쪽 아래

# 전체 종이 검사 시작 (0,0)부터 N x N 영역
divide(0, 0, N)

# 결과 출력
print(white)
print(blue)
