class Stack:
    body = list()
    stack_size = 0
    def __init__(self, h):
        self.body = h
        self.stack_size = len(h)
    def push(self, num):
        self.body.append(num)
        self.stack_size += 1
    def pop(self):
        if self.stack_size == 0:
            return -1
        else:
            pop = self.body.pop(self.stack_size - 1)
            self.stack_size -= 1
            return pop
    def top(self):
        if self.stack_size == 0:
            return 0
        else:
            return self.body[self.stack_size - 1]
    def empty(self):
        if self.stack_size == 0:
            return 0
        else:
            return 1
    def size(self):
        return self.stack_size

def solution(arrangement):
    answer = 0
    stack = Stack(list())
    stack.push(arrangement[0])
    pipe = 1
    for i in range(1, len(arrangement)):
        if stack.top() == "(":
            if arrangement[i] == ")":
                pipe -= 1
                answer += pipe
                stack.push(arrangement[i])
            elif arrangement[i] == "(":
                pipe += 1
                stack.push(arrangement[i])
        elif stack.top() == ")":
            if arrangement[i] == ")":
                pipe -= 1
                answer += 1
                stack.push(arrangement[i])
            elif arrangement[i] == "(":
                pipe += 1
                stack.push(arrangement[i])
    return answer





arrangement = "()(((()())(())()))(())"
print(solution(arrangement))

"""
def solution(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')

    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer
    """