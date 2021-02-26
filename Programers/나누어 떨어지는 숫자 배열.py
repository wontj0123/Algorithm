def solution(arr, divisor):
    ans= []
    count=0
    for x in arr:
        if x % divisor == 0:
            ans.append(x)
            count+=1
    if count == 0:
        ans.append(-1)
        return ans
    ans.sort()
    return ans