def fits(box1, box2):
    for i in range(3):
        if box1[i] <= box2[i]:
            return False
    return True

def max_stack(boxes):
    boxes.sort(reverse=True)
    stack_map = {}
    max_height = 0
    for i in range(len(boxes)):
        height = create_stack(boxes, i, stack_map)
        max_height = max(max_height, height)
    print(max_height)


def create_stack(boxes, bottomi, stack_map):
    if bottomi in stack_map:
        return stack_map[bottomi]
    bottom = boxes[bottomi]
    max_height = 0
    for i in range(bottomi + 1, len(boxes)):
        if fits(bottom, boxes[i]):
            height = create_stack(boxes, i, stack_map)
            max_height = max(max_height, height)
    max_height += bottom[1]
    stack_map[bottomi] = max_height
    return max_height


boxes = [[6, 7, 8], [2, 3, 4], [5, 6, 2], [5, 5, 7], [3, 4, 5], [4, 5, 6], [1, 2, 2]]
max_stack(boxes)