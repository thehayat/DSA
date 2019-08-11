class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node
        self.prev =  Node


class CircularDoublyLinkedList:

    head = None
    def __init__(self, data):

        self.head = Node(data)

    def length(self):
        p1 = self.head
        count = 1
        while p1 != self.head:
            p1 = p1.next
            count += 1
        return count

    def isempty(self):
        if self.length:
            return False
        else:
            return True

    def search(self, element):
        p1 = self.head
        while p1.next != self.head:
            if p1.data == element:
                return True

            else:
                p1 = p1.next
        return False

    def insert_begining(self, data):
        # temp = Node(data)
        # p1 = self.head
        temp = Node(data)
        p1 = self.head
        temp.next = self.head
        self.head = temp
        while p1 != self.head:
            p1 = p1.next
        t1 = self.head
        t2 = t1.next
        temp.prev = t1
        temp.next = t2.prev
        t2.prev = temp
        p1.next = t1
        
        

    def insert_end(self, data):
        temp = Node(data)
        p1 = self.head
        while p1 == self.head:
            p1 = p1.next
        p1.next = temp
        temp.next = self.head

    def insert_middle_before(self, before, element):
        p1 = self.head
        temp = Node(element)
        while p1.next.data != before:
            p1 = p1.next
        t1 = p1
        temp.next = t1.next
        p1.next = temp

    def insert_middle_after(self, after, element):
        p1 = self.head
        temp = Node(element)
        while p1.data != after:
            p1 = p1.next.next
        t1 = p1
        temp.next = t1.next
        p1.next = temp

    def delete_start(self):
        if self.isempty():
            print("Underflow")
        else:
            p1 = self.head
            self.head = self.head.next
            while p1.next != self.head:
                p1 = p1.next

            t1 = self.head
            self.head = self.head.next
            p1.next = self.head
            t1.next = None

    def delete_end(self):
        p1 = self.head
        while p1.next.next != self.head:
            p1 = p1.next

        t1 = p1.next
        t2 = p1.next.next

        p1.next = t2
        t1.next = None

    def delete_element_before(self, before):
        p1 = self.head
        while p1.next.next.data != before:
            p1 = p1.next
        t1 = p1.next
        t2 = t1.next
        p1.next = t2
        t1.next = None

    def delete_element_after(self, after):
        p1 = self.head
        while p1.data != after:
            p1 = p1.next

        t1 = p1.next
        t2 = t1.next
        p1.next = t2
        t1.next = None

    def traverse(self):
        p1 = self.head
        print("="*100)
        print("HEAD --> ", end=" ")
        while p1.next != self.head:

            print("|{}|{}|{}| -->".format(None if not p1.prev else p1.prev.data ,p1.data,None if not p1.next else p1.next.data), end=" ")
            p1 = p1.next
        print("|{}|{}|{}| --> HEAD".format(None if not p1.prev else p1.prev.data ,p1.data,
                                        None if not p1.next else p1.next.data))
        print("=" * 100)


if __name__ == "__main__":

    s1 = CircularDoublyLinkedList("b")

    s1.insert_begining("a")
    # s1.insert_end("g")
    # s1.insert_middle_after("b", "c")
    # s1.insert_middle_before("g", "d")
    # s1.insert_middle_before("g", "e")
    # s1.insert_middle_before("g", "f")
    # s1.delete_end()
    # s1.delete_start()
    # s1.delete_element_before("d")
    # s1.delete_element_after("d")
    # s1.traverse()
    print("success")

  
