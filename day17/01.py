from collections import Counter


containers = []
with open('01.txt') as f:
    for line in f.readlines():
        containers.append(int(line))
containers.sort()


def search(target, children, total=0, result=0):
    while children:
        child = children.pop()
        current_total = total + child
        if current_total == target:
            result += 1
        elif current_total > target:
            continue
        else:
            result += search(target, children.copy(), current_total)
    return result


RESULTS = []


def search_2(target, children, path=None):
    global RESULTS
    if not path:
        path = []
    while children:
        child = children.pop()
        new_path = path.copy()
        new_path.append(child)
        path_sum = sum(new_path)
        if path_sum == target:
            RESULTS.append(new_path)
        elif path_sum > target:
            continue
        else:
            search_2(target, children.copy(), new_path)


if __name__ == '__main__':
    combo_total = search(150, containers.copy())
    print('Part 1:', combo_total)
    search_2(150, containers.copy())
    counts = Counter([len(x) for x in RESULTS])
    print('Part 2:', counts[min(counts.keys())])
