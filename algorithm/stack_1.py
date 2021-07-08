#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발(stack)

import math

def solution(progresses, speeds):

    answer = []
    last_commit = 0
    remaining_tasks = list(map(lambda x: 100 - x, progresses))  # set remain tasks
    remaining_days = [math.ceil(i / j) for i, j in zip(remaining_tasks, speeds)]
    for rd in remaining_days:
        if rd > last_commit:
            answer.append(1)
            last_commit = rd
        else:
            answer[-1] += 1
    return answer

