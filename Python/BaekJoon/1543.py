# 기본탐색
document = input() # 문장 입력
word = input() # 검색하려는 단어 입력

index = 0
result = 0

while len(document) - index >= len(word):
    if document[index:index + len(word)] == word: # 인덱스부터 단어의 길이 만큼 비교
        result += 1
        index += len(word)
    else:
        index += 1 # 단어가 없을 경우 한칸만 이동
print(result)