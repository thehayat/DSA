"Question"
# https://practice.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1/?ref=self


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

def pairWiseSwap(head):
    # code here
    if head:
        if head.next == None:
            return head
        
        current = head
        if not current.next:
            return head
        
        while (current != None):
            if not current.next:
                return head
            next_=current.next
            current.data, next_.data = next_.data, current.data
            current = next_.next
        return head
        
if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        llist.head = pairWiseSwap(llist.head)
        llist.printList()
        t -= 1