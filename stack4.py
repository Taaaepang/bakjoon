class Stack:
    body = list()
    stack_size = 0
    def __init__(self, body):
        self.body = body
        self.stack_size = len(body)
    def push(self, num):
        self.body.append(num)
        self.stack_size += 1
        return num
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
            return True
        else:
            return False
    def size(self):
        return self.stack_size

def solution(prices):
    answer = list()
    stack = Stack(list())
    info = list()
    for i in range(len(prices)-1, -1, -1):
        info.append([0, prices[i]])

    stack.push(info[0])
    answer.append(info[0][0])
    for i in range(1, len(prices)):
        if stack.top()[1] >= info[i][1]:
            if stack.size() >= 2:
                while stack.size() != 0:
                    num = stack.pop()
                    if num[1] >= info[i][1]:
                        info[i][0] += 1
                stack.push(info[i])
                answer.append(info[i][0])
            elif stack.top()[0] > 1:
                info[i][0] = stack.top()[0] + 1
                answer.append(info[i][0])
                stack.push(info[i])
            else:
                info[i][0] += 1
                stack.push(info[i])
                answer.append(info[i][0])
        elif stack.top()[1] < info[i][1]:
            info[i][0] += 1
            stack.push(info[i])
            answer.append(info[i][0])

    answer.reverse()
    return answer



def main():
    print(solution([1, 2, 3, 2, 3]))
    print(solution([3, 1, 4, 1, 2]))
    print(solution([3, 1, 2, 5, 4, 3, 6, 1, 2]))
if __name__ == "__main__":
    main()