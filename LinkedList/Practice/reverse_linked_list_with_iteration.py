def reverseList(self):
        previous = None
        while self.head != None:
            current = next_ = self.head
            next_ = current.next
            self.head= next_
            current.next = previous
            previous = current
            current = self.head
            
        self.head = previous

class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.lastNode = None
    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.lastNode = self.head
        else:
            new_node = node(val)
            self.lastNode.next = new_node
            self.lastNode = new_node
    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head
    reverse_List = reverseList
    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reverse_List()
        lis.printList()

''' This is a function problem.You only need to complete the function given below '''
#function Template for python3
"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""
# your task is to complete this function
# function shouldn't return anything
# use self.head to access head in the method
