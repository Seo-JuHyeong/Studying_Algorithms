n, m, k = map(int, input().split())  # 공백으로 구분하여 입력받기
data = list(map(int, input().split()))  # 여러개의 수를 공백으로 구분하여 입력받고 list형으로 저장
data.sort()  # 오름차순 정렬

max_value = data[n - 1]  # 가장 큰 수
second_max_value = data[n - 2]  # 가장 작은 수

count = int(m / (k + 1)) * k
count += m % (k + 1)

Sum = 0
Sum += count * max_value
Sum += (m - count) * second_max_value
print(Sum)
