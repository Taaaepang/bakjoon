def search(lists ,num):
    for i in range(len(lists)):
        if lists[i] == num:
            return 1
    return 0


def solution(n, lost, reserve):
    anwser = n
    lost.sort()
    reserve.sort()
    visited = [False] * len(reserve)
    while len(lost) != 0:
        stupid = lost.pop(0)
        i = 0
        if search(reserve, stupid):
            if visited[reserve.index(stupid)] == True:
                anwser -= 1
            else:
                visited[reserve.index(stupid)] = True
        else:
            while len(reserve) != 0:
                if (reserve[i] == stupid + 1 or reserve[i] == stupid - 1) and visited[i] == False:
                    visited[i] = True
                    break
                if i == len(reserve) - 1:
                    anwser -= 1
                    break
                i += 1
    return anwser

def main():
    solution(5, [4, 5], [3, 4])
   # solution(5, [2, 4], [3])
    #solution(3, [3], [1])
    #solution(3, [1, 2, 3], [1, 3])

if __name__ == "__main__":
    main()