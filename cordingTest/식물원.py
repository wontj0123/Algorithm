import sys
from os import kill
sys.stdin=open("flower.txt", "rt")
n =int(input())
flower= []
for _ in range(n):
    flower.append(list(map(int,input().split())))
print(flower)

Max=max(flower)
max_date=max(Max)
print(max_date)
#날짜를 세기 위해 0으로 초기화
date = [0]*(max_date+1)
print(date)
count =0
for i in flower:
    for j in range(i[0],i[1]):
        #시작 날부터 끝날 전까지 배열에 1로 세팅
        date[j]=1;
#1로 세팅된 날 카운트 해서 출력
for count_date in date:
    if count_date == 1:
        count +=1;
print(count)