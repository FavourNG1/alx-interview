def canUnlockAll(boxes):
    if not boxes:
        return False

    num_boxes = len(boxes)
    keys = [0]  # Start with the key to the first box (index 0)
    unlocked = {0}  # Set to keep track of unlocked boxes

    while keys:
        key = keys.pop()
        box = boxes[key]

        # Add new keys from the current box
        for new_key in box:
            if 0 <= new_key < num_boxes and new_key not in unlocked:
                keys.append(new_key)
                unlocked.add(new_key)

    return len(unlocked) == num_boxes
