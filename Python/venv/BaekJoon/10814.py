# 기본 정렬 나이순 정렬(정렬)
n = int(input())

array = []
for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

array = sorted(array, key = lambda x: x[0])
for i in array:
    print(i[0], i[1])