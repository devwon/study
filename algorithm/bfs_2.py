#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://programmers.co.kr/learn/courses/30/lessons/43162
# Network(bfs)

def bfs(computers, check, i, n):
    dq = deque()
    dq.append(i)    # 큐에 현재 번호를 넣음

    while len(dq) > 0:  # 큐가 빌때까지 루프를 돌림
        cur_idx = dq.pop()  # 큐에 있는 노드 번호를 팝
        check[cur_idx] = True   # 큐에 있는 노드를 체크함

        for k in range(0, n):   # 현재 노드와 연결된 노드를 탐색
            # 방문하지 않았고 연결된 노드이면 dq에 추가
            if not check[k] and computers[cur_idx][k] == 1:
                dq.append(k)

def solution(n, computers):
    answer = 0
    check = [False for i in range(n)]   # 노드들 체크

    for i in range(0, n):
        if not check[i]:   # 현재 노드번호가 방문하지 않은 상태일때
            bfs(computers, check, i, n)
            answer += 1

    return answer

