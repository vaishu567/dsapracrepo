class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# a = Node(13)
# b = Node(56)
# print(a)
# print(b)
# a.next = b
# print(a.data)
# print(b.data)
# print(a.next.data)

# this is simple procedure but not optimised:


def takeInput():
    inputlist = [int(ele) for ele in input().split()]
    # before going to each part of the list i am initializing my head as none
    # if no input is there then head is none we'll return head
    head = None
    for currData in inputlist:
        if currData == -1:
            break
        newNode = Node(currData)
        # checking if head is none:
        if head is None:
            head = newNode
        # in else condition we are making connections to form linkedlist
        else:
            # if head is not None then we are at second element
            # we will point curr to head and mark curr.next as newNode:
            # if curr.next is not None then we will move curr to curr.next and point its next to newNode.
            curr = head
            # through this while loop we are moving our curr pointer till its next is None.
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head

# we want to print linkedlist like this 1->2->3->4->5->6->None
# we are going to implement printLL(head) and pass head as a parameter


def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end="")
        head = head.next
    print("None")
    return




# optimised printing of ll:
def inputOPLL():
    inputlist = [int(ele) for ele in input().split()]
    head=None
    tail=None
    for currele in inputlist:
        if currele==-1:
            break
        newNode=Node(currele)
        if head is None and tail is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head




# print ith node in ll:
def ithNode(i,head):
    count=0
    curr=head
    while count<i and curr!=None:
        count+=1
        curr=curr.next
    if i==count:
        return curr





# insert new node at ith position:
def insertnode(i,head,data):
    prev=i-1
    curr=i
    newNode=Node(data)
    if i>0:
        prevNode=ithNode(prev,head)
        currNode=ithNode(curr,head)
        prevNode.next=newNode
        newNode.next=currNode
        printLL(head)
    else:
        currNode = ithNode(curr, head)
        newNode.next=currNode
        head=newNode
        printLL(head)
    return head


def length(head):
    count=0
    curr=head
    while curr.next is not None:
        curr=curr.next
        count+=1
    return [count+1,curr]


# head = inputOPLL()
# print(length(head))

# delete node specified at index:
def deleteNode(head,i):
    if i==0:
        head=head.next
        printLL(head)
    elif i>length(head):
        return None
    else:
        prev=i-1
        currNode=ithNode(i,head)
        prevNode=ithNode(prev,head)
        prevNode.next=currNode.next
        printLL(head)
    return head





# insert node using recursion:
def recinsertnode(head,i,data):
    if i<0:
        return head
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return newNode
    if head is None:
        return None
    sub=recinsertnode(head.next,i-1,data)
    head.next=sub
    return head


    
# 1->2->3->4->5->None
# lastNto first:
def lastNtoFirst(n,head):
    curr=head
    lenh,tail=length(head)
    if n < 0 or n > lenh:
        return head
    count=0
    while count<lenh-n-1:
        count+=1
        curr=curr.next

    h2=curr.next
    curr.next=None
    tail.next=head
    printLL(h2)
    return h2
head = inputOPLL()
print(lastNtoFirst(6,head))
    
        

        




        

        





