class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    head = None
    def __init__(self):

        self.head = None
        self.size = 0

    def isempty(self):
        if self.size == 0:
            return False
        elif self.size < 0:
            pass
        else:
            return True

    def search(self, element):
        count = 0
        if self.size == 0:
            print("LinkedList Empty")
            return False, count
        elif self.size == 1:
            p1 = self.head
            if p1.data == element:
                return True, count
        else:
            p1 = self.head
            while p1.next != self.head:
                count += 1
                if p1.data == element:
                    return True, count

                else:
                    p1 = p1.next
            else:
                if p1.data == element:
                    return True,count
                return False, None

    def insert_begining(self, data):
        temp = Node(data)
        if self.size == 0:
            self.head = temp
            temp.next = self.head
            self.size +=1
        elif self.size == 1:
            first_node = self.head
            temp.next = first_node
            self.head = temp
            first_node.next = temp
            self.size +=1
        else:
            self.head = temp
            temp.next = self.head
            first_node = self.head
            second_node = self.head.next
            second_last_node = first_node
            while second_last_node.next != self.head:
                second_last_node = second_last_node.next

            temp.next = first_node
            self.head = temp
            second_last_node.next = temp
            self.size +=1

    def insert_end(self, data):
        temp = Node(data)
        first_node = self.head
        second_last = self.head
        while second_last != self.head:
            second_last = second_last.next

        second_last.next = temp
        temp.next = first_node
        self.size +=1

    def insert_middle_before(self, before, element):
        if self.size == 0:
            print("LinkedList Undeflow")
            return 0
        elif self.size == 1 and self.search(before)[0]:
            self.insert_begining()

        elif self.size > 1 and self.search(before)[0]:

            middle_ = Node(element)
            
            middle_previous = self.head
            while middle_previous.next.data != before:
                middle_previous = middle_previous.next
            middle_after = middle_previous.next
            middle_.next = middle_after
            middle_previous.next = middle_
            self.size +=1
            
            

        elif self.size >= 1 and self.search(before)[1]:
            print("Given before element not found ")
            return 0

    def insert_middle_after(self, after, element):
        if self.size == 0:
            print("LinkedList Undeflow")
            return 0

        elif self.size == 1 and self.search(after)[0]:
            self.insert_end(element)

        elif self.size > 1 and self.search(after)[0]:
            middle_ = self.head
            middle_after = self.head.next
            temp = Node(element)
            while middle_.data != after:
                middle_ = middle_.next.next
            middle_.next = temp
            temp.next = middle_after
            self.size +=1

        elif self.size >= 1 and not self.search(after)[1]:
            print("Given After Element not found ")
            return 0

    def delete_start(self):
        if self.size == 0:
            print("LinkedList UnderFlow !")
            return 0
        else:
        
            last = self.head
            while last.next != self.head:
                last = last.next
            
            first_node = self.head
            self.head = self.head.next
            last.next = self.head
            first_node = None
            self.size -=1

    def delete_end(self):
        if self.size == 0:
            print("LinkedList UnderFlow !")
            return 0
        else:
            first_node = self.head
            second_last = self.head

            while second_last.next.next != self.head:
                second_last = second_last.next

            last_node = second_last.next
            second_last.next = first_node
            last_node.next = None
            self.size -=1

    def delete_element_before(self, before):

        if self.size < 2:
            print("LinkedList Underflow")
            return 0

        elif self.size == 2 and self.search(before)[1] == 2:
            self.delete_start()

        elif self.size > 2 and self.search(before)[0]:
            if self.head.next.data == before:
                self.delete_start()
            else:
                before_previous = self.head
                while before_previous.next.next.data != before:
                    before_previous = before_previous.next
                
                before_ = before_previous.next
                before_after = before_.next
                before_previous.next = before_after
                before_.next = None
                self.size -=1

        elif self.size > 2 and not self.search(before)[0]:
            print("No element exist before given element.")

    def delete_element_after(self, after):

        if self.size == 0:
            print("LinkedList Underflow")
            return 0

        elif self.size == 1:
            self.delete_start()

        elif self.size == 2 and self.search(after)[1] == 1:
            self.delete_end()

        elif self.size > 2 and self.search(after)[0]:

            after_previous = self.head
            after_ = self.head.next
            after_next = after_.next

            while after_previous.data != after:
                after_previous = after_previous.next

            after_previous.next = after_next
            after_.next = None
            self.size -=1

        elif self.size > 2 and not self.search(after)[0]:
            print("No element exist before given element.")

    def traverse(self):
        p1 = self.head
        print("="*100)
        print("HEAD --> ", end=" ")
        while p1.next != self.head:

            print("|{}|{}| -->".format(p1.data,
                                       None if not p1.next else p1.next.data), end=" ")
            p1 = p1.next
        print("|{}|{}| --> HEAD".format(p1.data,
                                        None if not p1.next else p1.next.data))
        print("=" * 100)


if __name__ == "__main__":

    s1 = CircularSinglyLinkedList()

    s1.insert_begining("a")
    print("After Inserting a at start")
    s1.traverse()
    print()
    s1.insert_end("g")
    print("After Inserting g at last")
    s1.traverse()
    print()
    s1.insert_middle_after("a", "c")
    print("After Inserting c after a")
    s1.traverse()
    print()
    s1.insert_middle_before("g", "d")
    print("After Inserting d before g")
    s1.traverse()
    print()
    s1.insert_middle_before("g", "e")
    print("After Inserting e before g")
    s1.traverse()
    print()
    s1.insert_middle_before("g", "f")
    print("After Inserting f before g")
    s1.traverse()
    print()
    s1.delete_end()
    print("After Delete from end ")
    s1.traverse()
    print()
    s1.delete_start()
    print("After Delete from start ")
    s1.traverse()
    print()
    s1.delete_element_before("d")
    print("After Delete element before d ")
    s1.traverse()
    print()
    s1.delete_element_after("d")
    print("After Delete element after d ")
    s1.traverse()
    print()

