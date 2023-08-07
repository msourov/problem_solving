# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def counter(lst):
    print(len(set(lst)))
    print(*Counter(lst).values(), end='\n')

if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    counter(lst)
