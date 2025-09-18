def checkmate(board: str):
    grid = [list(row) for row in board.splitlines() if row.strip() != ""]
    if not grid:
        print("Fail")
        return

    n = len(grid)

    # หา King
    king_pos = None
    for i in range(n):
        for j in range(len(grid[i])):
            if grid[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return

    kx, ky = king_pos

    # ตรวจขอบเขต
    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < len(grid[x])

    # ตรวจ Pawn (เฉียงขึ้นและลง)
    for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
        x, y = kx + dx, ky + dy
        if in_bounds(x, y) and grid[x][y] == 'P':
            print("Success")
            return

    # Bishop / Queen (แนวทแยง)
    for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
        x, y = kx, ky
        while True:
            x += dx
            y += dy
            if not in_bounds(x, y):
                break
            if grid[x][y] != '.':
                if grid[x][y] in ['B','Q']:
                    print("Success")
                    return
                break

    # Rook / Queen (แนวตรง)
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        x, y = kx, ky
        while True:
            x += dx
            y += dy
            if not in_bounds(x, y):
                break
            if grid[x][y] != '.':
                if grid[x][y] in ['R','Q']:
                    print("Success")
                    return
                break

    # Knight
    for dx, dy in [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]:
        x, y = kx + dx, ky + dy
        if in_bounds(x, y) and grid[x][y] == 'N':
            print("Success")
            return

    # ถ้าไม่มีตัวไหนโจมตี King
    print("Fail")