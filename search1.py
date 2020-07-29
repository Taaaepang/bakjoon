def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5] * 2000
    person2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    score = [0] * 3
    for i in range(len(answers)):
        if answers[i] == person1[i]:
            score[0] += 1
        if answers[i] == person2[i]:
            score[1] += 1
        if answers[i] == person3[i]:
            score[2] += 1
    max_score = max(score)
    for i in range(len(score)):
        if max_score == score[i]:
            answer.append(i+1)
    return answer

def main():
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 3, 2, 4, 2]))

if __name__ == "__main__" :
    main()