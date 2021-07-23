https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter

def solution(clothes):
    # My code
    case = 1
    c_dict = {}
    for c in clothes:
        if c[1] in c_dict.keys():
            c_dict[c[1]].append(c[0])
        else:
            c_dict[c[1]] = [c[0]]
    
    for d in c_dict:
        case *= len(c_dict[d]) + 1
    case -= 1
    return case
    
    # 6 line
#     case = 1
#     c = Counter([x[1] for x in clothes])

#     for v in c.values():
#         case *= v+1
#     case -= 1
#     return case

    # 1 line
    from functools import reduce

    def solution(c):
        return reduce(lambda x,y:x*y,[a+1 for a in Counter([x[1] for x in c]).values()])-1