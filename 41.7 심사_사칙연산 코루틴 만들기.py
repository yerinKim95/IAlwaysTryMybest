'''
41.7 심사문제: 사칙연산 코루틴 만들기
표준 입력으로 사칙연산 계산식이 여러 개 입력됩니다.
다음 소스 코드에서 각 계산식의 결과를 구하는 코루틴을 만드세요.
계산식은 문자열 형태이며 값과 연산자는 공백으로 구분됩니다.
그리고 값은 정수로 변환하여 사용하고, 나눗셈은 / 연산자를 사용하세요.

judge_coroutine.py
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________

expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()
예
입력
1 + 2, 4 - 9
결과
3
-5
입력
3 * 4, 10 / 5, 20 + 39
결과
12
2.0
59
'''
def calc():
    result = 0

    while True:
        exp = (yield result)
        exp = exp.split(' ')

        if exp[1] == '+' : result = int(exp[0]) + int(exp[2])
        if exp[1] == '-' : result = int(exp[0]) - int(exp[2])
        if exp[1] == '*' : result = int(exp[0]) * int(exp[2])
        if exp[1] == '/' : result = int(exp[0])/int(exp[2])



expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()

