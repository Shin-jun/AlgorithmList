# 이진 탐색
n, c = list(map(int, input().split(' ')))

array = []
# 들어온 n값(집의 위치) 오름차순 정렬
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = array[1] - array[0] # 집 사이의 거리 min
end = array[-1] - array[0] # 집 사이의 거리 Max
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid
    else: # c개 이상의 공유기를 설치할 수 없는 경우
        end = mid - 1
print(result)