from collections import deque
import sys
from os import kill
sys.stdin=open("up_side_down.txt","rt")

n= int(input())
arr = []
print(n)
for i in range(n):
    arr.append(int(input()))
arr.sorted(reverse=True)
for i in arr:
    print(i,end=" ")
