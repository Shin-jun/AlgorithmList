# 재귀함수
import copy

def recursive(array, n):
    if len(array) == n:
        operators.list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()


test_case = int(input())
for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([], n - 1) # 연산자 생성

    integers = [i for i in range(1, n+1)] # 수 대입

    for operators in operators_list:
        string = "" # 식
        for i in range(n -1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0: # 공백제거 값이 0이라면
            print(string)
    print()