import sys
sys.stdin = open("스마트 물류")

n, k = map(int, sys.stdin.readline().split())
# 로봇 = H, 부픔 = P
r = list(str(sys.stdin.readline()))
cnt = 0
for i in range(n):
    if r[i] == "P":
        for j in range(i-k,i+k+1):
            if j < 0 or j > n-1:
                continue
            elif r[j] == "H":
                cnt += 1
                r[j] = "A"
                break

print(cnt)
