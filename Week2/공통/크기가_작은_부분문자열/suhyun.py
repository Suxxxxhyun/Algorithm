def solution(t, p):
    answer = 0
    for idx in range(0, len(t) - len(p) + 1):
        s = ""
        for i in range(idx, idx + len(p)):
            s += t[i]
        if int(s) <= int(p):
            answer += 1
    return answer

t = "3141592"
p = "271"
print(solution(t, p))