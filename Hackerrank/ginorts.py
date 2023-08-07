def ginorts(string):
    dic = {'l':[], 'u':[], 'o':[], 'e':[]}
    for i in string:
        if ord(i) in range(97, 122+1):
            dic['l'].append(i)
        elif ord(i) in range(65, 90+1):
            dic['u'].append(i)
        elif ord(i) in [49, 51, 53, 55, 57]:
            dic['o'].append(i)
        elif ord(i) in [48, 50, 52, 54, 56]:
            dic['e'].append(i)
    return ''.join([''.join(sorted(i)) for i in dic.values()])
    
if __name__ == '__main__':
    print(ginorts(input()))
