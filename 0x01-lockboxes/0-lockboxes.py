#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""
from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    queue = deque([0])

    while queue:
        box_idx = queue.popleft()
        for key in boxes[box_idx]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)