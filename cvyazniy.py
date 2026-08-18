class Node(): #класс узел
    def __init__(self, data):
        self.data = data #данные в узле
        self.next = None #ссылка на следующий узел


class Linked_list(): #класс список
    def __init__(self):
        self.head = None #ссылка на первый узел
        self.tail = None #ссылка на последний
        self.length = 0

    def append(self, data):
        new_node = Node(data) 
        if not self.head:
            self.head = new_node 
            return
        now = self.head #текущий узел
        while now.next: #если следующий существует,
            now = now.next  
        now.next = new_node
        self.tail = new_node
        self.length += 1

    


    def remove_value(self, value):
        pass

    def remove_dublicate(self):
        pass

    def __iter__(self):
        return LinkedIterator(self.head, self.length)

    def merge(linked_list_1, linked_list_2):
        pass

    def compression(linked_list):
        pass

class LinkedIterator():
    def __init__(self, head, length):
        self.head = head
        self.index = 0
        self.length = length

    def __iter__(self):
        return self
    
    def __next__(self): 
        if(self.index > self.length):
            raise StopIteration
        current = self.head
        for i in range(self.index):
            current = current.next
        self.index += 1
        return current.data

ll1 = Linked_list()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)

for item in ll1:
    print(item)