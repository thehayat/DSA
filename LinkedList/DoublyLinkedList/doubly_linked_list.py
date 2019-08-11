class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    head = None
    def __init__(self, data):

        self.head = Node(data)

    def length(self):
        p1 = self.head
        count = 0
        while p1:
            p1 = p1.next
            count += 1
        return count

    def isempty(self):
        if self.length():
            return False
        else:
            return True

    def traverse(self):
        p1 = self.head
        print("="*100)
        print("HEAD --> ", end=" ")
        while p1:

            print("|{}|{}|{}| -->".format(None if not p1.prev else p1.prev.data,
                                          p1.data, None if not p1.next else p1.next.data), end=" ")
            p1 = p1.next
        print()
        print("=" * 100)

    def reverse_traverse(self, p1):
        if not p1:
            return ""
        return self.reverse_traverse(p1.next) + "|{}|{}|{}| ---> ".format(None if not p1.next else p1.next.data, p1.data, None if not p1.prev else p1.prev.data,
                                                                          )

    def search(self, element):
        p1 = self.head
        while p1:
            if p1.data == element:
                return True

            else:
                p1 = p1.next
        return False

    def insert_begining(self, data):
        p1 = self.head
        temp = Node(data)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_end(self, data):
        p1 = self.head
        temp = Node(data)
        while p1.next:
            p1 = p1.next
        p1.next = temp
        temp.prev = p1

    def insert_middle_before(self, before, element):
        p1 = self.head
        temp = Node(element)
        while p1.next.data != before:
            p1 = p1.next
        temp.prev = p1
        temp.next = p1.next
        p1.next = temp
        temp.next.prev = temp

    def insert_middle_after(self, after, element):
        p1 = self.head
        temp = Node(element)
        while p1.data != after:
            p1 = p1.next.next
        temp.prev = p1
        temp.next = p1.next
        p1.next = temp
        temp.next.prev = temp

    def delete_start(self):
        if self.isempty():
            print("Underflow")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.head.prev = None

    def delete_end(self):
        p1 = self.head
        while p1.next.next != None:
            p1 = p1.next
        temp = p1.next
        p1.next = None
        temp.prev = None

    def delete_element_before(self, before):
        p1 = self.head
        while p1.next.next.data != before:
            p1 = p1.next

        t1 = p1.next
        p1.next = t1.next
        p1.next.prev = p1
        t1.prev = None
        t1.next = None

    def delete_element_after(self, after):
        p1 = self.head
        while p1.data != after:
            p1 = p1.next

        t1 = p1.next
        p1.next = t1.next
        p1.next.prev = p1
        t1.prev = None
        t1.next = None

    def return_head(self):
        return self.head


if __name__ == "__main__":

    s1 = DoublyLinkedList("a")
    s1.insert_begining("b")
    s1.insert_begining("c")
    s1.insert_begining("d")
    s1.insert_end("e")
    s1.insert_middle_before("a", "d")
    s1.insert_middle_after("a", "g")
    print("Traversal From Start")
    s1.traverse()
    print("Traversal From End")
    print("="*100)
    print(s1.reverse_traverse(s1.return_head())+" HEAD ")
    print("="*100)
# s1.delete_start()
# s1.delete_end()
# s1.delete_element_before("a")
# s1.delete_element_after("a")
