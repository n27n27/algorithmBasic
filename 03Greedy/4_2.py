num = 5 # int(input())
count = 0
for i in range(num + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1    
print(count)
print("="*50)

countH = 0
countA = 0
noCount = 0

for i in range(num + 1):
    if '3' in str(i):
        countH += 1

for i in range(60):
    for j in range(60):
        if '3' in str(i) + str(j):
            countA += 1
        else:
            noCount += 1
countA = countA * (num + 1)
noCount = noCount * countH

print(countA + noCount)

