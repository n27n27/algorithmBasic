# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 반복회수 K 입력받기

## 입력조건
# 첫째 줄에 (2 <= N <= 1,000), (1 <= M <= 10,000), (1 <= K <= 10,000) 의 자연수
# 둘째 줄에 N개의 자연수가 주어진다. 자연수는 1 이상 10,000 이하의 수
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

## 출력조건
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

# 데이터 정렬
data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:

    for i in range(k):        
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break        
    
    result += second
    m -= 1

print(result)
