import sys
from os import kill
from collections import deque
sys.stdin=open("histogram.txt", "rt")
histogram = list(map(int,input().split()))
print(histogram)
his=[(idx,height) for idx, height in enumerate (histogram)]
rlt = []
for i in his:
    for j in his:
        n=min(i[1],j[1])
        m=j[0]-i[0]-1
        rlt.append(n*m)
ans=max(rlt)
print(ans)