'''그룹단어 체커
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서,
각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고
중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.

예제 입력 1 
3
happy
new
year
예제 출력 1 
3
예제 입력 2 
4
aba
abab
abcabc
a
예제 출력 2 
1
예제 입력 3 
5
ab
aa
aca
ba
bb
예제 출력 3 
4
예제 입력 4 
2
yzyzy
zyzyz
예제 출력 4 
0
예제 입력 5 
1
z
예제 출력 5 
1


'''
# 일단 먼저 나왔던 단어가 다른 단어로 바뀌고 나서
#다시 나오면 그룹단어가 아니다!
# 나머지는 그룹단어다 로 하면될거같은데

trial = int(input())
word = []
for i in range(trial):
    word.append(input())

count = trial        

for i in word:  # 처음 단어 abcabc에서
    for j in range(len(i)): # 5번 돕니다 j = 0이면
        if i.rfind(i[j]) - i.find(i[j]) +1 != i.count(i[j]):
            # 3- 0 +1
            count -= 1
            break

print(count)
