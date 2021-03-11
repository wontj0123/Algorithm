import sys
from os import kill
from collections import deque
sys.stdin=open("histogram.txt", "rt")
histogram = list(map(int,input().split()))
rlt = []
n= len(histogram)
for i in histogram:
    for j in histogram:
        n = min(histogram[i],histogram[j])
        m =j-i-1
        rlt.append(n*m)
print(max(rlt))
