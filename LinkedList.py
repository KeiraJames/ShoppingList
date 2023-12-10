class Node:
    """ This is the Node class """
    def __init__(self, data):
        self.data = data
        self.next_pointer = None


class LinkedList(Node):
    """ This is the LinkedList class """
    def __init__(self):
        self.head = None
        self.size = 0

    
    def is_empty(self):
        return self.size == 0

    
    def get_size(self):
        return self.size

    
    def get_head(self):
        return self.head.data

    
    def check_range(self, index):
        if index < 0 or index > self.size-1:
            raise Exception("Index out of bounds")

    
    def set(self, index, data):
        self.check_range(index)
        temp = self.head

        for i in range(index):
            temp = temp.next

        removed_data = temp.data
        temp.data = data

        return removed_data

    
    def add(self, data):
        n = Node(data)

        if self.is_empty():
            self.head = n
        else:
            temp = self.head
            while temp.next_pointer is not None:
                temp = temp.next_pointer

            temp.next_pointer = n

        self.size += 1

    
    def add_specific_index(self, data, index):
        self.check_range(index)

        n = Node(data)

        if index == 0:
            n.next_pointer = self.head
            self.head = n
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next_pointer

            n.next_pointer = temp.next_pointer
            temp.next_pointer = n

        self.size += 1

    
    def remove_specific_index(self, index):
        self.check_range(index)

        if index == 0:
            return None
        elif index == 0:
            removed_data = self.head.data
            self.head = None
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next_pointer

            removed_data = temp.next_pointer.data
            temp.next_pointer = temp.next_pointer.next_pointer

        self.size -= 1
        
        return removed_data

    
    def remove(self):
        if self.is_empty():
            print("List is empty.")
            return

        temp = self.head
        for i in range(self.size-2):
            temp = temp.next_pointer

        removed_data = temp.next_pointer.data
        temp.next_pointer = None
        self.size -= 1

        return removed_data

    
    def display_list(self):      
        temp = self.head
        count = 1
        while temp is not None:
            print(str(count) + ".\t" + str(temp.data))
            temp = temp.next_pointer
            count += 1
