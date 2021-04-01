import sys
sys.stdin = open("stack.txt","rt")
n= int(input())
for i in range(n):
    arr=[]
    s=input()
    cnt=0
    for j in range(len(s)):
        if s[j]=='(':
            arr.append(s[j])
            cnt +=1
        else:
            if len(arr)==0:
                cnt-=1
                break
            arr.pop()
            cnt-=1
    if cnt == 0:
        print("yes")
    else:
        print("no")
