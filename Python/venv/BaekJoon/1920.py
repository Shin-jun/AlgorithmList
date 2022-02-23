# 고급 자료구조 수찾기(해시, 배열, 구현)
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print("1")