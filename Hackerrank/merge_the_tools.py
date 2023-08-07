def merge_the_tools(string, k):
    # your code goes here
    u = []
    t = ''
    for i in range(0, len(string), k):
        u.append(string[i:i+k])
    for i in range(len(u)):
        for j in u[i]:
            if j not in t:
                t += j
            else:
                continue
        print(t)
        t = ''


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
