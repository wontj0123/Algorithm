def solution(priorities, location):

    #index 번호와 가중치를 같이 큐에 저장
    queue =  [(i,p) for i,p in enumerate(priorities)]

    answer = 0
    while True:
        cur = queue.pop(0)
        #any를 사용하면 한가지라도 있으면 true
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer