n, m, k = map(int, input().split())  # 공백으로 구분하여 입력받기
data = list(map(int, input().split()))  # 여러개의 수를 공백으로 구분하여 입력받고 list형으로 저장
data.sort()  # 오름차순 정렬

max_value = data[n - 1]  # 가장 큰 수
second_max_value = data[n - 2]  # 가장 작은 수
Sum = 0  # 합 (결과 값)

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기
        # 반복문이 시작되자마자 아래 조건문을 거치게 함으로써 이후 중복되는 조건문을 쓰지 않게 됨.
        if m == 0:  # m이 0이라면 반복문 탈출!
            break
        Sum += max_value  # Sum에 가장 큰 값 더하기
        m -= 1  # 더할 때 마다 m값 1씩 빼기
    if m == 0:
        break
    Sum += second_max_value  # Sum에 두번 째로 큰 값 더하기
    m -= 1  # 더할 때 m 값에 1 빼기
    # if m == 0:    !!  12번 line 반복문이 시작되자마자 조건문을 거치게 함으로써 사용하지 않아도 됨
    #     break
print(Sum)
