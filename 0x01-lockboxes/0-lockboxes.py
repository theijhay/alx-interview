#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.

    :param boxes:
    :return: True or False
    """
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
