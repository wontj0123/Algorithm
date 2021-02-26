def solution(s):
    answer = True
    n = len(s)
    p= 0
    y= 0
    S= s.upper()
    for x in S:
        if x == "P":
            p+=1
        elif x=="Y":
            y+=1
    if p == y:
        return True
    else:
        return False