import sys
from os import kill

sys.stdin=open("input.txt","rt")
n,m,k = map(int,input().split())# 변수개수, 덧셈 횟수, 연속 회수
data = list(map(int,input().split()))
data.sort()
print(data)
print(n,m,k)
first = data[n-1]
second= data[n-2]
print(first,second)
result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result+=first
        m-=1
    if m == 0:
        break
    result += second
    m-=1
print(result)


