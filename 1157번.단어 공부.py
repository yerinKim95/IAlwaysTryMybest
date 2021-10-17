'''
단어 공부
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서
가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을
작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을
대문자로 출력한다. 단, 가장 많이 사용된 알파벳이
여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi
예제 출력 1 
?
예제 입력 2 
zZa
예제 출력 2 
Z
예제 입력 3 
z
예제 출력 3 
Z
예제 입력 4 
baaa
예제 출력 4 
A
'''

word = input().upper()
word_set = list(set(word))
cnt = []

for i in word_set:
    cnt.append(word.count(i))
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_set[cnt.index(max(cnt))])
'''
가장 많이 사용된 알파벳을 출력하기
가장 많이 사용된 알파벳 고르기
RAINNING
for i in range(len(word)):
word.count(word[i])
새로운 []에 씨우고
큰 숫자들 word에서 찾고 비교
같으면 결과는 같은거 내고
다르면 결과는 ?

MY ORIGINAL ANSWER
word = input()
word = word.upper()
word = list(word)
count = word.copy()
most = 0
newWord= []
for i in range(len(word)):
    count[i] = word.count(word[i])


most = max(count)       # 가장 높은숫자

for i in range(len(word)): # max 인 문자들 찾으러간다
    if count[i] == most:
        newWord.append(word[i]) 
result = newWord[0]
for i in newWord:
    if i != result:
        result = '?'
        break
print(result)

TOOK FOREVERRRRR IT SAYS

'''


