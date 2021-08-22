# 거스름돈 입력받기
n = int(input("거스름돈을 입력하세요"))
count = 0

# 큰 단위부터 차례로 확인
coins = [500, 100, 50, 10]

for coin in coins:    
    n %= coin
    count += 1

print(count)

