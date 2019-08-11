""" Question """
# https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1/?ref=self


def rotateList(head, k):
    # if head:
    # code here1
    temp=head
    temp1=head
    count=0
    while count<k-1 and (temp is not None):
        temp=temp.next
        count=count+1
    if temp is None:
        return
    temp2 = temp
    while temp.next is not None:
        temp=temp.next
    temp.next = temp1
    head = temp2.next
    temp2.next  = None
    return head


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
        while(temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print("")


if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while(t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = rotateList(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa

''' This is a function problem.You only need to complete the function given below '''
# Your task is to complete this function
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
# This function should rotate list counter-
# clockwise by k and return new head (if changed)
