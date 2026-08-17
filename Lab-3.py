//1.Implementing Stack using Linked List 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

top = None

def push(value):
    global top
    newNode = Node(value)
    newNode.next = top
    top = newNode
    print(value, "pushed into stack")

def pop():
    global top
    if top is None:
        print("Stack Underflow")
        return
    print(top.data, "popped from stack")
    top = top.next

def display():
    temp = top
    print("Stack:", end=" ")
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

push(10)
push(20)
push(30)
display()
pop()
display()

//2.Implementing Queue using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

front = rear = None

def enqueue(value):
    global front, rear
    newNode = Node(value)

    if rear is None:
        front = rear = newNode
    else:
        rear.next = newNode
        rear = newNode

    print(value, "enqueued into queue")

def dequeue():
    global front, rear
    if front is None:
        print("Queue is empty")
        return

    print(front.data, "dequeued from queue")
    front = front.next

    if front is None:
        rear = None

def display():
    temp = front
    print("Queue:", end=" ")
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

enqueue(10)
enqueue(20)
enqueue(30)
display()
dequeue()
display()