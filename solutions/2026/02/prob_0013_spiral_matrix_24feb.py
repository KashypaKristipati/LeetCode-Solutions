def spiralMatrixIII(R: int, C: int, r0: int, c0: int, spiralTypes: int) -> List[List[int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    directions_str = ['right', 'down', 'left', 'up']
    directions_map = {direction: directions_str[i] for i, direction in enumerate(directions)}
    directions_map['right'] = 0
    directions_map['down'] = 1
    directions_map['left'] = 2
    directions_map['up'] = 3

    def get_next_direction(direction, steps):
        next_direction_index = (direction + steps) % 4
        return directions[next_direction_index]

    def get_next_position(r, c, direction):
        if direction == 0:  # right
            return r, c + 1
        elif direction == 1:  # down
            return r + 1, c
        elif direction == 2:  # left
            return r, c - 1
        elif direction == 3:  # up
            return r - 1, c

    def get_spiral_matrix(R, C, r0, c0, direction, spiral_type):
        matrix = [[0] * C for _ in range(R)]
        matrix[r0][c0] = spiral_type
        directions_to_visit = [direction]
        r, c = r0, c0
        while directions_to_visit:
            next_r, next_c = get_next_position(r, c, directions_to_visit[0])
            if 0 <= next_r < R and 0 <= next_c < C and matrix[next_r][next_c] == 0:
                matrix[next_r][next_c] = spiral_type
                directions_to_visit.append(get_next_direction(directions_to_visit[0], 1))
                r, c = next_r, next_c
            else:
                directions_to_visit.pop(0)
                if directions_to_visit:
                    direction = directions_to_visit[0]
                    r, c = get_next_position(r, c, direction)
        return matrix

    matrix = get_spiral_matrix(R, C, r0, c0, 0, spiralTypes)
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
    return matrix