import sys
from os import kill
sys.stdin=open("떡볶이 떡 만들기.txt", "rt")
n, m =map(int,input().split())
print(n,m)
arr = list(map(int,input().split()))
print(arr)
start = 0
end = max(arr)
result = 0

while start<=end:
    tot = 0
    mid = (start + end) // 2
    for x in arr:
        if mid <x:
            tot += x-mid
    if tot < m:
        end = mid -1
    else:
        result = mid
        start = mid +1
print(result)


