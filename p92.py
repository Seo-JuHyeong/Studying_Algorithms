n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

max_value = data[n - 1]
second_max_value = data[n - 2]
Sum = 0

while True:
    for i in range(k):
        if m == 0:
            break
        Sum += max_value
        m -= 1
    if m == 0:
        break
    Sum += second_max_value
    m -= 1

print(Sum)
