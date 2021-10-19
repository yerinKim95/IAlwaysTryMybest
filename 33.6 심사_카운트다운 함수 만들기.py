'''
33.6 심사_카운트다운 함수 만들기

표준 입력으로 정수가 입력됩니다.
다음 소스 코드를 완성하여 함수 c를 호출할 때마다
숫자가 1씩 줄어들게 만드세요.
여기서는 함수를 클로저로 만들어야 합니다.
정답에 코드를 작성할 때는 def countdown(n):에 맞춰서 들여쓰기를 해주세요.

judge_closure.py
def countdown(n):
________________
________________
________________
________________
________________
________________

n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')
예
입력
10
결과
10 9 8 7 6 5 4 3 2 1 
입력
20
결과
20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
'''
def countdown(n): 
    def movingtonext():
        global n    
        n = n - 1
        return n + 1
    return movingtonext

n = int(input())        # Entering 10
 
c = countdown(n)        # c = using the method countdown
for i in range(n):      # 10 times
    print(c(), end=' ') 
