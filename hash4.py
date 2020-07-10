def solution(genres, plays):
    dic = {}
    dic2 = {}
    answer = list()
    for i in range(len(genres)):
        if dic.get(genres[i]):
            dic[genres[i]] += plays[i]
            dic2[genres[i]].append(plays[i])
        else:
            dic[genres[i]] = plays[i]
            dic2[genres[i]] = list()
            dic2[genres[i]].append(plays[i])
    index = sorted(dic.values(), reverse=True)
    key, value = dic.keys(), dic.values()
    temp = list()
    i = 0
    j = 0
    while True:
        tmp = index.pop(0)
        for key, value in dic.items():
            if value == tmp:
                temp.append(key)
                break
        if len(index) == 0:
            break
    for i in temp:
        list1 = sorted(dic2[i], reverse=True)
        answer.append(plays.index(list1[0]))
        answer.append(plays.index(list1[1]))

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))