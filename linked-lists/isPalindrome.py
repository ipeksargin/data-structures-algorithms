"""A palindrome is a word or a sequence that is the same from the front as from the back."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_data):
        new_data = Node(new_data)
        if self.head == None:
            self.head = new_data
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_data

    def isPalindrome(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        current = self.head

        while current:
            node = stack.pop()
            if current.data != node:
                return False
            current = current.next
            return True


    def printList(self):
        if self.head == None:
            return "Empyt list"
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next


mylist = LinkedList()
mylist.append("A")
mylist.append("B")
mylist.append("C")
mylist.append("D")
print(mylist.isPalindrome())

mylist_two = LinkedList()
mylist_two.append("R")
mylist_two.append("A")
mylist_two.append("D")
mylist_two.append("A")
mylist_two.append("R")
print("For second list:")
print(mylist_two.isPalindrome())


