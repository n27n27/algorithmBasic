
n, k = map(int, input().split())

count = 0

while(n != 1):
    if(n % k == 0):
        n //= k        
    else:
        n -= 1
    count += 1

print(count)

n, k = map(int, input().split())
count = 0

while True:
    target = (n // k) * k
    count += (n - target)
    n = target

    if n < k:
        print("탈출 전 n의 값 {0}, 및 회수 {1}".format(n, count))
        break
    n //= k
    count += 1
    print("현재까지 회수: ", count)

count += (n - 1)
print(count)




