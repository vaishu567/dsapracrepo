# creatiing binary trees:
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None
btn1=BinaryTree(1)
btn2=BinaryTree(2)
btn3=BinaryTree(3)
btn4=BinaryTree(4)
btn5=BinaryTree(5)
btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5


def printTreeDetailed(root):
    if root == None:
        return 
    print(root.data, end=":")
    if root.left!=None:
        print("L", root.left.data, end=",")
    if root.right!=None:
        print("R", root.right.data, end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)
printTreeDetailed(btn1)