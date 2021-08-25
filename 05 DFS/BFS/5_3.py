def recursiveFunction(count):
    print("재귀 함수를 호출합니다.")
    count += 1
    if count == 10:
        return
    recursiveFunction(count)

recursiveFunction(0)