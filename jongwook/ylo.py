class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def rotate(self, k):
        if k < 1:
            print("invalid k")
            return
        curr = self.head

        count = 1
        while count < k and curr is not None:
            curr = curr.next
            count += 1

        if curr is None:
            print("Invalid K")
            return

        kthnode = curr  # 값 할

        while curr.next is not None:    # 리스트 마지막으로 가면 다시 리스트 앞으로 가도록
            curr = curr.next            # curr is pointing to next

        curr.next = self.head           # if curr.next is none it points to head

        self.head = kthnode             # change the head to kthnode

        while curr.next is not kthnode: # k-1 th node should now point to none
            curr = curr.next

        curr.next = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        line = ''
        while (temp):
            line += str(temp.data) + '->'
            temp = temp.next
        line += 'END'
        print(line)



llist = LinkedList()

for i in range(60, 0, -10):
    llist.push(i)

print("Given Linked List")
llist.printList()
llist.rotate(2)

print("\nRotated Linked List")
llist.printList()