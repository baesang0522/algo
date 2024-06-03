def find_intersection(s, t):
    a, b, e = s
    c, d, f = t

    deter = a*d-b*c

    if deter == 0:
        return None

    x = (b*f-e*d) / (a*d-b*c)
    y = (e*c-a*f) / (a*d-b*c)

    if x != int(x) or y != int(y):
        return None

    return [x, y]


def display_coordinates(coordinates):
    # 좌표 중 최대값과 최소값을 찾아 배열의 크기를 결정
    zipped_data = list(zip(*coordinates))
    min_values = [min(group) for group in zipped_data]
    max_values = [max(group) for group in zipped_data]
    max_x, min_x = max_values[0], min_values[0]
    max_y, min_y = max_values[1], min_values[1]

    size_x = max_x - min_x + 1
    size_y = max_y - min_y + 1

    grid = [['.' for _ in range(size_x)] for _ in range(size_y)]

    for x, y in coordinates:
        grid[max_y - y][x - min_x] = '*'

    result = [''.join(row) for row in grid]
    return result

def solution(line):
    inters = []

    for a in line:
        for b in line:
            if a == b:
                continue
            inter = find_intersection(a, b)
            if inter:
                inters.append(inter)

    inters = list(set(map(lambda x: (int(x[0]), int(x[1])), inters)))

    return display_coordinates(inters)











