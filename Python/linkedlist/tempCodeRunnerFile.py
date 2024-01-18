class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(13)
b=Node(56)
print(a)
print(b)
a.next=b
print(a.data)
print(b.data)
print(a.next.data)

# this is simple procedure but not optimised:
def takeInput():
    inputlist=[int(ele) for ele in input().split()]
    # before going to each part of the list i am initializing my head as none
    # if no input is there then head is none we'll return head
    head=None
    for currData in inputlist:
        if currData==-1:
            break
        newNode=Node(currData)
        # checking if head is none:
        if head is None:
            head=newNode
        # in else condition we are making connections to form linkedlist
        else:
        # if head is not None then we are at second element
        # we will point curr to head and mark curr.next as newNode:
        # if curr.next is not None then we will move curr to curr.next and point its next to newNode.
            curr=head 
            # through this while loop we are moving our curr pointer till its next is None.
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    return head
head=takeInput()