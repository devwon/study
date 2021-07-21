# https://programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록

def solution(phone_book):
    # 내 코드
    # for i in phone_book:
    #     for j in range(1, len(phone_book)):
    #         if i in phone_book[j] and i != phone_book[j]:
    #             return False      
    # return True
    
    # hash 정석
    # hash_map = {}
    # for phone_number in phone_book:
    #     hash_map[phone_number] = 1
    # for phone_number in phone_book:
    #     temp = ''
    #     for number in phone_number:
    #         temp += number
    #         if temp in hash_map and temp != phone_number:
    #             return False
    # return True
    
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True