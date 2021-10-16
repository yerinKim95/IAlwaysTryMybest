'''
문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후
출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고,
두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

출력
각 테스트 케이스에 대해 P를 출력한다.

예제 입력 1 
2
3 ABC
5 /HTP
예제 출력 1 
AAABBBCCC
/////HHHHHTTTTTPPPPP

'''
T = int(input())                    # 1<= T <= 1000
R = []
S = []
NewS = ''
for i in range(T):
    r, s = map(str, input().split(' ')) # 1<=R<=8       1<=len(S)<20
    r = int(r)
    R.append(r)
    S.append(s)
# T = 2     R[0] = 3   S[0]= ABC    R[1] = 5    S[1] = /HTP

for i in range(T):
    #출력은 AAABBBCCC /////HHHHHTTTTTPPPPP
    #일단 case 1:
    NewS = ''
    S[i] = list(S[i]) # S[0] =['A','B','C']
    for j in range(len(S[i])):  #총 세글자
        for k in range(R[i]):   # 총 세번 반복
            NewS +=(S[i][j])
            #NewS.join(S[i][j])  
    print(NewS)
        
                   
