def solution(genres, plays):
    dic = {}
    answer = []
    for i in range(len(plays)):
        if dic.get(genres[i]):
            dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = 0
            dic[genres[i]] = plays[i]
    key, value = dic.keys(), dic.values()
    temp = list(value)
    temp = temp.index(max(temp))
    g = list(key)[temp]
    val = list()
    for i in range(len(genres)):
        if genres[i] == g:
            val.append(plays[i])
    temp = sorted(val, reverse=True)
    for i in range(0, 2):
        answer.append(plays.index(temp[i]))
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))