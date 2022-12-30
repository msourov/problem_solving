class Node:
    def __init__(self, key=None):
        self.data = key
        self.fw = None

class LinkedList:
    def __init__(self):
        self.head = None
    def getLength(self):
        n = self.head
        l = 0
        while n.fw is not None:
            l +=1
            n = n.fw
        return l
    def getIndex(self, index):
        cur = self.head
        count = 0
        while cur:
            if count == index:
                return cur.key
            count += 1
            cur = cur.fw
        return -1
    def addFirst(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.fw = self.head
        self.head = new_node
    def addLast(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.fw != None:
            cur = cur.fw
        cur.fw = new_node
    def InsertAtIndex(self, index, key):
        if self.head is None:
            return
        elif index == len:
            self.addLast(key)
        else:
            new_node = Node(key)
            cur = self.head
            count = 0
            while cur.fw is not None:
                if count == index:
                    new_node.fw = cur.fw
                    cur.fw = new_node
                count += 1
    def RemoveAtIndex(self, index):
        if self.head == None:
            return
        elif index in range(0, len):
            if index == 0:
                self.head = None
                return
            else:
                cur = self.head
                count = 0
                while cur.fw is not None:
                    if count == index:
                        cur.fw = cur.fw.fw
                        return
                    count += 1
        else:
            return None
    def CheckPalindrome(self):
        cur = self.head
        lst = [cur.key]
        while cur.next is not None:
            cur = cur.fw
            lst.append(cur.key)

        lst.reverse()
        temp = self.head
        i = 0
        while temp.fw is not None:
            if temp.key != lst[i]:
                return 'Not palindrome'
            temp = temp.fw
            i += 1
        return 'Palindrome'

ll = LinkedList()
len = ll.getLength()
prompt = True
while prompt == True:
    print("""
        Enter 1 to get index:
        Enter 2 to add at first:
        Enter 3 to add at last
        Enter 4 to insert at index:
        Enter 5 to remove at index:
        Enter 6 to check palindrome:
        Enter 7 to exit:
    """)
    ans = int(input())
    if ans == 1:
