import sys
from os import kill

sys.stdin=open("input.txt", "rt")
n,m = map(int,input().split())
result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_val= min(data)
    result = max(result,min_val)
print(result)