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
    def search(self, num):
        temp_body = self.body.copy()
        temp = Stack(temp_body)
        while temp.size() != 0:
            if temp.top() > num:
                return temp.size()
            else:
                temp.pop()
        if temp.size() == 0:
            return 0
def solution(heights):
    answer = []
    top = Stack(list())
    temp = heights.copy()
    while True:
        if len(temp) == 0:
            break
        shoot = temp.pop(0)
        if top.top() > shoot:
            answer.append(top.size())
            top.push(shoot)
        else:
            answer.append(top.search(shoot))
            top.push(shoot)

    return answer


heights = [6, 9, 5, 7, 4]
print(solution(heights))

'''
def solution(heights):
    stack = []
    stack.append(0)
    max_pos = 1
    max_val = heights[0]

    for i in range(1,len(heights)):
        if heights[i] >= max_val:
            stack.append(0)
            max_pos = i+1
            max_val = heights[i]
        if heights[i] < max_val:
            stack.append(max_pos)
        if heights[i] < heights[i-1]:
            max_pos = i
            max_val = heights[i-1]
            stack.pop()
            stack.append(max_pos)

    return stack
    '''