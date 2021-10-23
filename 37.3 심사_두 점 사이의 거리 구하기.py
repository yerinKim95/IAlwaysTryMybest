'''
37.3 심사문제: 두 점 사이의 거리 구하기
표준 입력으로 x, y 좌표 4개가 입력되어
Point2D 클래스의 인스턴스 리스트에 저장됩니다.
여기서 점 4개는 첫 번째 점부터 마지막 점까지 순서대로 이어져 있습니다.
다음 소스 코드를 완성하여 첫 번째 점부터 마지막 점까지 연결된
선의 길이가 출력되게 만드세요.

judge_line_length.py
import math
 
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

_____________________
_____________________
_____________________
_____________________

print(length)
예
입력
10 10 20 20 30 30 40 40
결과
42.42640687119285
입력
100 100 200 200 300 300 400 400
결과
424.26406871192853
'''
import math
 
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

line1 = math.sqrt(math.pow(p[1].x-p[0].x,2) + math.pow(p[1].y - p[0].y ,2))
line2 = math.sqrt(math.pow(p[2].x-p[1].x,2) + math.pow(p[2].y - p[1].y ,2))
line3 = math.sqrt(math.pow(p[3].x-p[2].x,2) + math.pow(p[3].y - p[2].y ,2))
length = line1 + line2 + line3

print(length)
