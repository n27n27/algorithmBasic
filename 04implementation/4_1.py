## 입력조건
# 첫째 줄에 공간의 크기를 나타내는 n이 주어진다.
n = int(input("공간의크기입력(숫자)"))
# 두번째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.
plans = input("계획서입력(LRUD)".split())
# 초기 좌표값 설정
x, y = 1, 1

# 이동방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 이동수행
    x, y = nx, ny
print(x, y)
