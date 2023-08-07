import itertools
s = input()
x=[i for i in s]
for key, group in itertools.groupby(s, lambda x: x):
    print((len(list(group)), int(key)), end=' ')
