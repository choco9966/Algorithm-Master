def solution(dirs):
    visited = set()
    cmd = {'U':(0, 1), 'L':(-1, 0), 'R':(1, 0), 'D':(0, -1)}
    x, y = 0, 0

    for dir in list(dirs):
        dir_x, dir_y = cmd[dir]
        if abs(x + dir_x) <= 5 and abs(y + dir_y) <= 5:
            next_x, next_y = x+dir_x, y+dir_y
            if (x, y, next_x, next_y) not in visited:
                visited.add((x, y, next_x, next_y))
                visited.add((next_x, next_y, x, y))
            x, y = next_x, next_y
            
    return len(visited)/2
