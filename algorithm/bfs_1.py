#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버(bfs)

def solution(numbers, target):
    from collections import deque

    answer = 0
    queue = deque([(0, 0)])  # sum, level
    while queue:
        s, lv = queue.popleft()
        if lv > len(numbers):
            break
        elif lv == len(numbers) and s == target:
            answer += 1
        queue.append((s + numbers[lv - 1], lv + 1))
        queue.append((s - numbers[lv - 1], lv + 1))
    return answer

