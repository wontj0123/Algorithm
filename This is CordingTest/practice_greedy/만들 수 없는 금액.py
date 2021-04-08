import sys
sys.stdin = open("만들 수 있는 금액.txt","rt")

n = int(input())
data = list(map(int,input().split()))
data.sort()

target = 1
for x in data:
    #만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

#만들 수 없는 금액 출력
print(target)