#!/usr/bin/python3
"""canUnlockAll module:
contains the function canUnlockAll"""


def canUnlockAll(boxes):
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
