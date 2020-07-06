from _collections import *
def solution(phone_book):
    temp = phone_book.copy()
    for i in range(len(phone_book)):
        temp2 = phone_book[i]
        temp[i] = "x"
        for j in range(len(phone_book)):
            a1 = phone_book[i]
            b1 = temp[j]
            if a1 == temp[j][:len(a1)]:
                return False
            else:
                continue
        temp[i] = temp2
    return True

"""
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
"""



phone_book = ["119", "97674223", "1195524421"]

print(solution(phone_book))