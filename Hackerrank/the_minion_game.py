def minion_game(string):
    # your code goes here
    k_point = 0
    s_point = 0
    vowels = 'AEIOU'
    for i in range(len(string)):
        if string[i] in vowels:
            k_point += (len(string)-i)
        else:
            s_point += (len(string)-i)       
    if k_point>s_point:
        print(f'Kevin {k_point}')
    elif k_point<s_point:
        print(f'Stuart {s_point}')
    else:
        print('Draw')
 
if __name__ == '__main__':
    s = input()
    minion_game(s)
