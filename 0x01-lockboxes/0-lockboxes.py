#!/usr/bin/python3
"""canUnlockAll module:
contains the function canUnlockAll"""


def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = {0}  # Set of unlocked box indices
    keys = set(boxes[0])  # Set of available keys from the first box

    def unlock_boxes(keys):
        new_keys = set()
        for key in keys:
            if key < n and key not in unlocked:
                unlocked.add(key)
                new_keys.update(boxes[key])
        return new_keys

    while keys:
        keys = unlock_boxes(keys)

    return len(unlocked) == n
