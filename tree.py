#creating a node
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#inserting
def inserting(root,key):
    if root == None:
        return Node(key)
    if key < root.data:
        root.left = inserting (root.left,key)
        
    else:
        root.right=inserting (root.right,key)
    return root

#level order traversal
def levelorder(root):
    if root == None:
        return
    q = [root]
    while q:
        node = q.pop(0)
        print(node.data, end = " ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

#minimum and maximum
def max1(root):
    temp = root
    while temp.right:
        temp = temp.right
    return temp.data

def min1(root):
    if root.left == None:
        print(root.data)
    else:
        min1(root.left)


#inordrer traversal
def inorder(root):
    if root == None:
        return
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

#pre order 
def preorder(root):
    if root == None:
        return
    else:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


#post order
def postorder(root):
    if root == None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
    
#primary number
def primarynum(root):
    if root == None:
        return
    else:
        primarynum(root.left)
        if primarynumhelper:
            print(root.data)
        primarynum(root.right)

def primarynumhelper(n):
    for i in range(1,n+1):
        if n%i == 0:
            count+=1

        if count == 2:
            return True
        else:
            return False

#inserting elements
root = None
root = inserting(root,30)
inserting(root,4)
inserting(root,60)
inserting(root,50)
inserting(root,7)
print(root.left.data)
levelorder(root)
print("\n",max1(root))
min1(root)
print("inorder")
inorder(root)
print("preorder")
preorder(root)
print("postorder")
postorder(root)
print("primary number")
primarynum(root)