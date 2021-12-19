class node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    
    def append(self, value):
        if self.head == None:
            self.head = node(value)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node(value)
    def insert_at(self, value, index):
        temp = node(value)
        if index == 0:
            temp.next = self.head
            self.head = temp
            return
        prev = self.head
        for i in range(index-1):
            prev = prev.next
            
        temp.next = prev.next
        prev.next = temp
            
    def print_list(self):
        if self.head == None:
            print("list is empty")
        
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev = self.head
        for i in range(index-1):
            prev = prev.next
        current = prev.next
        prev.next = current.next
        
        
    def count(self, h = 0, n = 1):
        if h == 0:
            h = self.head
        if h.next != None:
            return self.count(h.next, n+1)
        else:return n
            
        
        
