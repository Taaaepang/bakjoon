def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        if dic.get(clothes[i][1]):
            dic[clothes[i][1]] += 1
        else:
            dic[clothes[i][1]] = 1
    for value in dic.values():
        answer *= value + 1
    return answer - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))

'''
headgear = 2
eyewear = 1
answer = 1

yellow_hat = y
blue... = b
g... = g

y, b, g, yb, gb, x(아무 것도 안입는 경우 x)
1 * 3 * 2 = 6
answer - 1 = 5
[[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]

answer = 1
1 * 4 = 4
4 - 1 = 3
'''