def remove_greater_node(node):
    current = node
    next_ = node
    max_ = node.data
    while current != None:
        next_ = current.next
        if next_.data > max_:
            max_= next_.data
            node = next_
            current = None
    node
    return node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
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

    def search(self, element):
        p1 = self.head
        while p1:
            if p1.data == element:
                return True

            else:
                p1 = p1.next
        return False

    def insert_begining(self, data):
        # ref = self.head
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insert_end(self, data):
        temp = Node(data)
        p1 = self.head
        while p1.next:
            p1 = p1.next
        p1.next = temp

    def insert_middle_before(self, before, element):
        p1 = self.head
        temp = Node(element)
        while p1.next.data != before:
            p1 = p1.next
        temp.next = p1.next
        p1.next = temp

    def traverse(self):
        p1 = self.head
        while p1:
            print("{}-->".format(p1.data), end=" ")
            p1 = p1.next
        print()

    def reverse_traverse(self, p1):

        if not p1:
            return ""

        return self.reverse_traverse(p1.next) + "{} ".format(p1.data)
        

    def reverse_llist(self, node):

        if node.next == None:
            self.head = node
            return self.head
        self.reverse_llist(node.next)
        first = node
        next_ = first.next
        next_.next = node
        node.next = None
        
    def insert_middle_after(self, after, element):
        p1 = self.head
        temp = Node(element)
        while p1.data != after:
            p1 = p1.next.next
        temp.next = p1.next
        p1.next = temp

    def delete_start(self):
        if self.isempty():
            print("Underflow")
        else:
            temp = self.head
            self.head = self.head.next
            temp = None

    def delete_end(self):
        p1 = self.head
        while p1.next.next != None:
            p1 = p1.next
        p1.next = None

    def delete_element_before(self, before):
        p1 = self.head
        while p1.next.next.data != before:
            p1 = p1.next
        temp = p1.next.next
        p1.next = temp
        temp = None

    def delete_element_after(self, after):
        p1 = self.head
        while p1.data != after:
            p1 = p1.next
        temp = p1.next.next
        p1.next = temp
        temp = None

    def get_head(self):
        return self.head


if __name__ == "__main__":
    
    s1 = SingleLinkedList(3)
    s1.insert_begining(2)
    s1.insert_begining(6)
    s1.insert_begining(5)
    s1.insert_begining(11)
    s1.insert_begining(10)
    s1.insert_begining(15)
    s1.insert_begining(12)
    temp = remove_greater_node(s1.get_head())
    print("success")
    

    # s1.traverse()

    # s1.reverse_llist(s1.get_head())
    # s1.traverse()

    # print(s1.search("e"))
    # print(s1.length())
    # s1.traverse()
    # s1.insert_middle_before("b", "j")
    # s1.traverse()
    # s1.insert_middle_after("a", "g")
    # s1.traverse()
    # s1.delete_start()
    # s1.traverse()
    # s1.delete_element_before("b")
    # s1.traverse()
    # s1.delete_element_after("b")
    # s1.traverse()
    # s1.delete_end()
    # s1.traverse()
