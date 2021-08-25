stack = []

# 삽입5, 삽입2, 삽입3, 삽입7, 삭제, 삽입1, 삽입4, 사게
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])
