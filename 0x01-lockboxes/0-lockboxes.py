#!/usr/bin/python3
"""Determines if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes=[]):
    """Tells if a box can be unlocked
    """
    if not boxes:
        return False

    box_set = set([0])
    for index, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != index:
                box_set.add(key)

    if len(box_set) != len(boxes):
        return False

    return True
