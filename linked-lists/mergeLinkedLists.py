from singleLinkedList import Node, LinkedList


def mergedLists(firstlist, secondlist, mergedList):
    currentFirst = firstlist.head
    currentSecond = secondlist.head

    while 1:
        if currentFirst is None:
            mergedList.insertLast(currentSecond)
            break
        if currentSecond is None:
            mergedList.insertLast(currentFirst)
            break
        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None # mergeslist = 1->None
            mergedList.insertLast(currentFirst)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insertLast(currentSecond)
            currentSecond = currentSecondNext


#creating first list
a = Node(1)
b = Node(3)
c = Node(4)
firstlist = LinkedList()
firstlist.insertLast(a)
firstlist.insertLast(b)
firstlist.insertLast(c)

#creating second list
d = Node(2)
e = Node(5)
f = Node(7)
secondlist = LinkedList()
secondlist.insertLast(d)
secondlist.insertLast(e)
secondlist.insertLast(f)

print("Printing first list")
firstlist.PrintList()
print("Printing second list")
secondlist.PrintList()

mergedList = LinkedList()
mergedLists(firstlist, secondlist, mergedList)
print("Printing merged list")
mergedList.PrintList()


