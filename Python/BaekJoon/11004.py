# 고급정렬 알고리즘 K번쨰 수
n, k = map(int, input().split())
array = list(map(int, input().split()))
array = sorted(array)
print(array[k-1])