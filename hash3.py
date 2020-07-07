def solution(clothes):
    answer = 0
    dictemp = dict(clothes)
    temp = 1
    answer += len(clothes)
    size = len(dic.keys())
    print(dic.values())
    if size > 1:
        for key in dic.keys():
            temp *= len(dic[key])
    else:
        temp = 0
    answer += temp
    temp = 1
    return answer




clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))