# 반복적으로 구현한 n!
def factorialIterative(n):
    result = 1

    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으루 구현한 n!
def factorialRecursive(n):
    if n <= 1:
        return 1
    return n * factorialRecursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print("반복적으로 구현:", factorialIterative(5))
print("재귀적으로 구현:", factorialRecursive(5))