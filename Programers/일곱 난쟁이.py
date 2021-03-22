import sys
from os import kill
sys.stdin=open("seven.txt", "rt")
arr = []
for i in range(9):
    arr.append(int(input()))
height= sum(arr)-100
for i in range(9):
    for j in range(i+1,9):
        if arr[i]+arr[j] == height:
            one = arr[i]
            two = arr[j]
arr.remove(one)
arr.remove(two)
arr.sort()
for i in arr:
    print(i)


