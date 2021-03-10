n=int(input())
#테이블 한쪽에 n명이 앉았을때 악수하는 경우의 수 구하기

#초기화
d= [0]*(n+1)
d[1]=1
d[2]=2
d[3]=3

for i in range(4,n+1):
    d[i]=d[i-2]+d[i-1]
print(d[n])