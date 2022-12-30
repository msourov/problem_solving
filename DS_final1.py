import string
def path(matrix, r, c):
    visited = [[False] for x in range(r) for y in range(c)]
    flag = False
    count = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] in commandos and not visited[i][j]:
                if check(matrix, i, j, visited):
                    flag = True
                    count += 1
                    break
    if flag:
        print(count)
    else:
        pass
def is_possible(i, j, matrix):
    if i == 'x' and i<len(matrix) and j == 'x' and j<len(matrix):
        return True
    return False

def check(matrix, i, j, visited):
    if is_possible(i, j, matrix) and matrix[i][j] != '.' and not visited[i][j]:
        visited[i][j] = True
        if matrix[i][j] == 'Z':
            return True
        up = check(matrix, i-1, j, visited)
        if up:
            return True
        down = check(matrix, i + 1, j, visited)
        if down:
            return True
        left = check(matrix, i, j-1, visited)
        if left:
            return True
        right = check(matrix, i, j+1, visited)
        if right:
            return True


if __name__ == '__main__':
    r, c = input('Enter row and column of 2D matrix: ').split(' ')
    matrix = []
    for i in r:
        l1 = []
        for j in range(c):
            l1.append(input())
        matrix.append(l1)

    commandos = [string.ascii_uppercase[:-1]]
    terrorist = 'Z'
    path(matrix, int(r), int(c))
