import sys
sys.setrecursionlimit(20000)

def check(p):
    stack = []
    for i in p:
        if len(stack) == 0:
            if i == '(':
                stack.append(i)
            else:
                return False
        else:
            if stack[len(stack)-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
    return True

def setting(p, a, t):
    if len(p) == 0:
        return a + t
    stack = []
    u = ""
    v = ""
    v_start = 0
    for i in range(len(p)+1):
        if i == 0:
            stack.append(p[i])
            u += p[i]
        elif len(stack) == 0:
            v_start = i
            break
        else:
            if stack[len(stack)-1] != p[i]:
                stack.pop()
                u += p[i]
            else:
                stack.append(p[i])
                u += p[i]
    v = p[v_start:]
    if check(u):
        a += u
        return setting(v, a, t)
    else:
        t = ""
        t += setting(v, "", t)
        temp = "(" + t + ")"
        for i in range(1, len(u) - 1):
            if u[i] == "(":
                temp += ")"
            elif u[i] == ")":
                temp += "("
        return a + temp

def solution(p):
    if check(p):
        return p
    answer = setting(p, "", "")
    return answer


def main():
    print(solution("(()())()"))
    print(solution(")("))
    print(solution("()))((()"))

if __name__ == '__main__':
    main()