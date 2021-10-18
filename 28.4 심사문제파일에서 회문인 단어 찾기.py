'''
회문판단

단어가 줄 단위로 저장된 words.txt 파일이 주어집니다.
words.txt 파일에서 회문인 단어를 각 줄에 출력하는 프로그램을 만드세요.
단어를 출력할 때는 등장한 순서대로 출력해야 합니다.
그리고 파일에서 읽은 단어는 \n이 붙어있으므로 \n을 제외한 뒤
회문인지 판단해야 하며 단어를 출력할 때도 \n이 출력되면
안 됩니다(단어 사이에 줄바꿈이 두 번 일어나면 안 됨).


apache
decal
did
neep
noon
refer
river

표준 출력
did
noon
refer

'''
lines = ['apache\n', 'decal\n','did\n' ,'neep\n',
                    'noon\n','refer\n','river\n']
with open ('words.txt', 'w') as file:
    file.writelines(lines)

with open ('words.txt', 'r') as file:
    words = file.readlines()

for i in words:
    i = i.strip('\n')
    if i == ''.join(reversed(i)):
        print(i)

