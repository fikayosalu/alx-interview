#!/usr/bin/python3
"""  0-lockboxes """

def canUnlockAll(boxes):
    """
    Checks if all boxes can be opened starting from box 0.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)            # Total number of boxes
    visited = set()           # Set to keep track of opened boxes
    stack = [0]               # Start with box 0 (already unlocked)

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for key in boxes[current]:
                if 0 <= key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n
