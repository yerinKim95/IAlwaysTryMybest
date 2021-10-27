'''
42.8 심사문제: HTML 태그 데코레이터 만들기
표준 입력으로 HTML 태그 이름 두 개가 입력됩니다.
다음 소스 코드에서 함수의 반환값을 HTML 태그로 감싸는 데코레이터를 만드세요.
HTML 태그는 웹 페이지에 사용하는 문법이며 <span>문자열</span>,
<p>문자열</p>처럼 <태그이름>으로 시작하며 </태그이름>으로 끝납니다.

judge_decorator.py
________________
________________
________________
________________
________________
________________

a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())
예
입력
p span
결과
<p><span>Hello, world!</span></p>
입력
b i
결과
<b><i>Hello, world!</i></b>
'''
class html_tag:
  def __init__(self, tag_name):
    self.tag_name = tag_name

  def __call__(self, func):
    def wrapper():
      return '<{0}>{1}</{0}>'.format(self.tag_name, func())
    return wrapper


a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())

'''
ANOTHER WAY

def html_tag(tag_name):
  def real_decorator(func):
    def wrapper():
      return '<{0}>{1}</{0}>'.format(tag_name,func())
    return wrapper
  return real_decorator
  '''
