'''
32.5 심사: 파일 이름을 한꺼번에 바꾸기
표준 입력으로 숫자.확장자 형식으로 된 파일 이름 여러 개가 입력됩니다
. 다음 소스 코드를 완성하여 파일 이름이 숫자 3개이면서
앞에 0이 들어가는 형식으로 출력되게 만드세요.
예를 들어 1.png는 001.png, 99.docx는 099.docx,
100.xlsx는 100.xlsx처럼 출력되어야 합니다.
그리고 람다 표현식을 사용해야 하며 출력 결과는 리스트 형태라야 합니다.
람다 표현식에서 파일명을 처리할 때는 문자열 포매팅과
문자열 메서드를 활용하세요.

judge_lambda.py
files = input().split()
 
print(________________)
예
입력
1.jpg 10.png 11.png 2.jpg 3.png
결과
['001.jpg', '010.png', '011.png', '002.jpg', '003.png']
입력
97.xlsx 98.docx 99.docx 100.xlsx 101.docx 102.docx
결과
['097.xlsx', '098.docx', '099.docx', '100.xlsx', '101.docx', '102.docx']

'''

files = input().split()
print(list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]),x.split('.')[1]) , files)))

'''
for i in range(len(files)):
    files[i] = files[i].split('.')
    files[i][0] = files[i][0].zfill(3)
   
print(files)

'''
'''
어려우니까 그냥 다 쪼개서 쓰고 나중에 합치자

'''
