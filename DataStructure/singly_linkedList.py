class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
    
    def __len__(self) -> int:
        return len(tuple(iter(self)))
    
    def __repr__(self):
        return "->".join([str(item) for item in self])

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        for i, node in enumerate(self):
            if i == index:
                return node
    def __setitem__(self, index, data):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data
    
    def insert_tail(self, data) -> Node:
        self.insert_nth(len(self), data)
    
    def insert_head(self, data) -> Node:
        self.insert_nth(0, data)
    
    def insert_nth(self, index: int, data) -> Node:
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
    
    def print_list(self) -> Node:
        print(self)
    
    def delete_head(self):
        return self.delete_nth(0)
    
    def delete_tail(self):
        return self.delete_nth(len(self)-1)
    
    def delete_nth(self, index: int = 0):
        if not 0 <= index <= len(self) - 1:
            raise IndexError("list index out of range")
        delete_node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        return delete_node.data
    
    def is_empty(self):
        return self.head is None
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            print('1 nextNode', next_node, 'current.next ', current.next, 'prev ', prev, ' current ', current )
            current.next = prev
            print('2 nextNode', next_node, 'current.next ', current.next, 'prev ', prev, ' current ', current )     
            prev = current
            print('3 nextNode', next_node, 'current.next ', current.next, 'prev ', prev, ' current ', current )
            current = next_node
            print('4 nextNode', next_node, 'current.next ', current.next, 'prev ', prev, ' current ', current )

        self.head = prev


linked_list = LinkedList()
linked_list.insert_head(10)
linked_list.insert_head(20)
linked_list.insert_head(30)
linked_list.insert_head(40)

print(linked_list.print_list())

linked_list.reverse()

linked_list.print_list()