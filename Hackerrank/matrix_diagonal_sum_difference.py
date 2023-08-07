from functools import reduce
def diagonalDifference(arr):
    d1 = reduce(lambda a, b: a+b, [v[i] for i, v in enumerate(arr)])
    d2 = reduce(lambda a, b: a+b, [v[len(v)-i-1] for i, v in enumerate(arr)])
    print(abs(d1-d2))
    

if __name__ == '__main__':
    n = int(input().strip())
    ar = []
    for _ in range(n):
        ar.append(list(map(int, input().rstrip().split())))
    diagonalDifference(ar)
    # arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    # diagonalDifference(arr)