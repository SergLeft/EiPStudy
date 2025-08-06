class Node:
    def __init__(self, wert):
        self.wert = wert
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = "["
        el = self.head
        while el is not None:
            s += str(el.wert)
            if el.next is not None:
                s += ", "
            el = el.next
        s += "]"
        return s

    def append(self, wert):
        node = Node(wert)
        if self.head is None:  # Leere Liste
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def prepend(self, wert):
        node = Node(wert)
        if self.head is None:  # Leere Liste
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def __contains__(self, wert):
        el = self.head
        while el is not None:
            if el.wert == wert:
                return True
            el = el.next
        return False

    def remove(self, value):
        el = self.head
        while el is not None:
            if el.wert == value:
                break
            el = el.next
        else:
            return
        if el.prev is None:
            self.head = el.next
        else:
            el.prev.next = el.next

        if el.next is None:
            self.tail = el.prev
        else:
            el.next.prev = el.prev
        del el # Wer mag :) https://stackify.com/python-garbage-collection/ für mehr Informationen

    def concat(self, other: "DoubleLinkedList"):
        if other.head is None:
            return
        if self.head is None:
            self.head = other.head
            self.tail = other.tail
            return
        self.tail.next = other.head
        other.head.prev = self.tail
        self.tail = other.tail

list = DoubleLinkedList()
list.prepend(1)
list.prepend(2)
list.append(3)
list.append(4)
print(list)
list.remove(3)
print(list)
print(4 in list)
print(5 in list)

list2 = DoubleLinkedList()
list2.prepend("macht")
list2.prepend("Programmieren")
list2.append("Spaß")
print(list2)
list.concat(list2)
print(list)

