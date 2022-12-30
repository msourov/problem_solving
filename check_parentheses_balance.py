class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def top(self):
        return self.items


def check_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


def check_if_balanced(string):
    global paren
    is_balanced = True
    index = 0
    s = Stack()
    while index < len(string) and is_balanced:
        paren = string[index]
        if paren in '({[':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not check_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty():
        if is_balanced:
            return 'Balanced'
        elif paren in ')}]':
            return 'Closing bracket overflow'
    if not s.is_empty(): #If unmatched or OBO stack will always contain at least one item
        if len(string) % 2 == 0:#Even because all opening bracket will have a closing bracket but at least one is different
            return 'Unmatched'
        else:
            return 'Opening bracket overflow'


print(check_if_balanced('{({})([])}}'))
print(check_if_balanced('[{{({})([])}}]'))
print(check_if_balanced('[{{({})([])})]'))
print(check_if_balanced('(()){{{[]}{[][]}}'))