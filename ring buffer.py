class cir_queue():

    def __init__(self, k):
        self.k = k
        self.queue = [0] * k
        self.head = self.tail = -1
        self.size = 0

    
    def append(self, data):

        if (self.next_index(self.tail + 1)== self.head):
            print("The cir_queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
            self.size += 1
        else:
            self.tail = self.next_index(self.tail + 1)
            self.queue[self.tail] = data
            self.size += 1
            


    def pop(self):
        if (self.head == -1):
            print("The cir_queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            self.size -= 1
        else:
            temp = self.queue[self.head]
            self.head = self.next_index(self.head + 1)
            self.size -= 1

            
    def next_index(self, i):
        return i%self.k

    def print_quque(self):
        if (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


n = int(input())

q = cir_queue(n)

while q.size < n:
    operation = input('operation: ')
    if operation == 'pop':
        q.pop()
    elif operation == 'append':
        q.append(int(input('Number: ')))

q.print_quque()
        
        
