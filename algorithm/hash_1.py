# https://programmers.co.kr/learn/courses/30/lessons/42576
# 완주하지 못한 선수

def solution(participant, completion):
    
    # 내 코드
#     participant = sorted(participant)
#     completion = sorted(completion)
#     completion.append('1')
    
#     for i in range(len(completion)):
#         if completion[i] != participant[i]:
#             return participant[i]
    
    # 개선
#     participant = sorted(participant)
#     completion = sorted(completion)
    
#     for p, c in zip(participant, completion):
#         if p != c:
#             return p
#     return participant[-1]
    
    # 초간결
    import collections
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]