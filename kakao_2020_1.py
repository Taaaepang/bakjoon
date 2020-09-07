import math
import sys
sys.setrecursionlimit(20000)
def process(s, i, start, end, qqqq):
    if end > len(s):
        for i in range(start, len(s)):
            qqqq.append([1, s[i]])
        return qqqq
    if len(qqqq) == 0:
        qqqq.append([1, s[start:end]])
    elif qqqq[len(qqqq)-1][1] == s[start:end]:
        qqqq[len(qqqq)-1][0] += 1
    elif qqqq[len(qqqq)-1][1] != s[start:end]:
        qqqq.append([1, s[start:end]])
    return process(s, i, end, end+i, qqqq)

def solution(s):
    answer = math.inf
    for i in range(0, int(len(s)/2)+1):
        temp = process(s, i+1, 0, i+1, [])
        cccc = []
        for j in temp:
            if j[0] > 1:
                t = str(j[0])
                for k in range(len(t)):
                    cccc.append(t[k])
            for k in range(len(j[1])):
                cccc.append(j[1][k])
        if answer > len(cccc):
            answer = len(cccc)
    return answer

def main():
    #print(solution("aabbaccc"))
    #print(solution("ababcdcdababcdcd"))
    #print(solution("abcabcdede"))
    print(solution("abcabcabcabcdededededede"))
    #print(solution("xababcdcdababcdcd"))
    #print(solution("a"))
    #print(solution("aaaaaaaaaaabbb"))
    print(solution("jeroen"))

if __name__ == '__main__':
    main()