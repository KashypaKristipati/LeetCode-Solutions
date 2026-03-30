def spiralMatrixIII(R, C, rows, cols):
    def get_next_position(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = (y + x) % 4
        return x + directions[dir_index][0], y + directions[dir_index][1]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    count = 0
    row_start = col_start = 0
    row_end = rows - 1
    col_end = cols - 1

    while True:
        for i in range(col_start, col_end + 1):
            if is_valid(i, row_start):
                count += 1
        row_start += 1
        if not is_valid(row_start, col_start) or row_start > row_end:
            break

        for i in range(row_start, row_end + 1):
            if is_valid(i, col_end):
                count += 1
        col_end -= 1
        if not is_valid(col_end, row_end) or col_end < col_start:
            break

        for i in range(col_end, col_start - 1, -1):
            if is_valid(i, row_end):
                count += 1
        row_end -= 1
        if not is_valid(row_end, col_end) or row_end < row_start:
            break

        for i in range(row_end, row_start - 1, -1):
            if is_valid(i, col_start):
                count += 1
        col_start += 1
        if not is_valid(col_start, row_start) or col_start > col_end:
            break

    return (count + 1) * rows * cols