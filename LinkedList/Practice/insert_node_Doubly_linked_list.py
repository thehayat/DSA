
def addNode(head, p, data):
    try:
        temp = Node(data)
        if head.next:
            p1 = head
            
            if p == 0:
                insert_after = p1
                insert_before = p1.next

                temp.prev = insert_after
                temp.next = insert_before
                insert_after.next = temp
                insert_before.prev = temp

                
            else:
                count = 0
                while count != p:
                    p1 = p1.next
                    count += 1
                
                insert_after = p1
                insert_before = p1.next

                temp.prev = insert_after
                temp.next = insert_before
                insert_after.next = temp
                insert_before.prev = temp
    
            
    except Exception as e:
        pass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def printList(self, node):
        while(node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while(node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = map(int, input().strip().split())
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        pos, data = map(int, input().strip().split())
        addNode(llist.head, pos, data)
        llist.printList(llist.head)
# Contributed by: Harshit Sidhwa


# function should add a new node after the pth position
# function shouldn't print or return any data
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''
