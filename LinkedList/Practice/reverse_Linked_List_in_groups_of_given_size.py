"""Question"""
# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1/?ref=self


def reverse(head, k):
    # Code here
    curr = head
    prev = None
    next_ = None
    count = k
    while(curr != None and count>0):
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
        count = count-1
    
    if next_ is not None:
        head.next = reverse(next_,k)
        
    return(prev)

    

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1

''' This is a function problem.You only need to complete the function given below '''
"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
