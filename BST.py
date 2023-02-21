class BST:
    def __init__(self,data): #for creating the node
        self.data=data
        self.right=None
        self.left=None
def insertion(rootnode,nodeval):
    if rootnode.data is None:
        rootnode.data=nodeval
    elif nodeval <= rootnode.data:
        if rootnode.left is None:
            rootnode.left=BST(nodeval)
        else:
            insertion(rootnode.left,nodeval)
    else:
        if rootnode.right is None:
            rootnode.right=BST(nodeval)
        else:
            insertion(rootnode.right,nodeval)
    #return "the node is successfully inserted :"
def preordertraversal(rootnode):
    if not rootnode:
        return 
    print(rootnode.data)
    preordertraversal(rootnode.left)
    preordertraversal(rootnode.right)
def inordertraversal(rootnode):
    if not rootnode:
        return 
    inordertraversal(rootnode.left)
    print(rootnode.data)
    inordertraversal(rootnode.right)
def postordertraversal(rootnode):
    if not rootnode:
        return 
    postordertraversal(rootnode.left)
    postordertraversal(rootnode.right)
    print(rootnode.data)
#searching a node in binary tree
def search(rootnode,nodeval):
    if rootnode.data==nodeval:
        print("the node presents :")
    elif(nodeval<rootnode.data):
        if rootnode.left.data==nodeval:
            print("the value is found :")
        else:
            search(rootnode.left,nodeval)
    else:
        if rootnode.right.data==nodeval:
            print("the value found :")
        else:
            search(rootnode.right,nodeval)

#finding minimun element in tree
def min(rootnode):
    if rootnode.left is None:
        return rootnode.data
    return min(rootnode.left)
#finding the maximum number in bst
def max(rootnode):
    if rootnode.right is None:
        return rootnode.data
    return max(rootnode.right)



# deleting the node
def deletion()
bst=BST(None)
x=[70,50,90,30,60,80,100,20,40]
for i in x:
    insertion(bst,i)
preordertraversal(bst)
print("\n")
inordertraversal(bst)
print("\n")
postordertraversal(bst)
ele=int(input("enter the element to found or not :"))
search(bst,ele)
print(min(bst))
print(max(bst))