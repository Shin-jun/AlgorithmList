# 기본탐색
n = int(input())

books = {} # 등장횟수를 구할 때는 딕셔너리가 좋다

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
target = max(books.values()) # 가장 큰값을 가져온다(등장 횟수)
array = []

for book, number in books.items():
    if number == target:
        array.append(book)

print(sorted(array[0]))
