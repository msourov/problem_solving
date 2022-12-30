class Node:
    def __init__(self, data=None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = None
        self.head.prev = None
    def get_node(self, index):
        cur = self.head
        if len_checker < 1:
            return cur
        for i in range(index+1):
            cur = cur.next
            if cur == self.head:
                return None
        return cur
    def check_list_len(self):
        i = 0
        temp = self.head
        while temp.next is not None:
            i += 1
            temp = temp.next
        return i

    def insertion(self, new_node, ref_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        ref_node.next.prev = new_node
        ref_node.next = new_node

    def deletion(self, val):
        cur = self.head
        while cur.next.data != val:
            cur = cur.next
        cur.next = cur.next.next

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    def display(self):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            print(cur_node.data, end=' ')
    def reverse_display(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        while temp.prev != None:
            print(temp.data, end=' ')
            temp = temp.prev


ll = linked_list()
prompt = True
print(type(ll))
while prompt == True:
    print("""
        Enter 1 to insert:
        Enter 2 to delete:
        Enter 3 to exit:
    """)
    ans = int(input())
    len_checker = ll.check_list_len()
    if ans == 1:
        if len_checker >= 1:
            val, index = map(int, input('Enter value and the position you want to add data separated by comma: ').split(','))
            new_node = Node(val)
        else:
            val = int(input('Enter the first value you want to add: '))
            new_node = Node(val)
            index = 0
        ref_node = ll.get_node(index)
        ll.insertion(new_node, ref_node)
    elif ans == 2:
        val = int(input('Which value you want to delete: '))
        ll.deletion(val)
    elif ans == 3:
        prompt = False
    else:
        print('Sorry! Couldn\'t understand!')
        continue

print(ll.display())
print(ll.reverse_display())
print(ll.length())

