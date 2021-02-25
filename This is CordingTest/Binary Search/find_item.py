import sys
from os import kill
sys.stdin=open("find_item.txt", "rt")

#page 198 이진탐색을 이용한 부품 탐색
def find_item(arr,target,start,end):

    while start<=end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif arr[mid]>target:
            end= mid-1
        else:
            start = mid+1
    return None
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
x = list(map(int, input().split()))


for i in x:
    result = find_item(arr,i,0,n-1)
    if result !=None:
        print("yes", end=" ")
    else:
        print("no", end=" ")

