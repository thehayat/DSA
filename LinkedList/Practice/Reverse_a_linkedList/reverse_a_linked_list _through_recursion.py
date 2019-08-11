
# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1/?ref=self
def reverseList():
    # Code here
    print(recur_reverse_list(head))

def recur_reverse_list(head):
    if not head:
        return ""
    temp = temp + " " + str(recur_reverse_list(head.next))
    return temp

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



    
