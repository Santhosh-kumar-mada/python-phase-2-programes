#creating a node of a tree
class Node:
    def __init__(san,data):
        san.data = data
        san.left = None
        san.right = None

#inorder traversal of a tree
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data , end=" ")
    inorder(root.right)

def inorder_prime(root):
    if root == None:
        return
    inorder(root.left)
    if prime(root.data):
        print(root.data)
    inorder(root.right)


#pre order traversal of a tree
def preorder(root):
    if root == None:
        return
    print(root.data ,end =" ")
    preorder(root.left)
    preorder(root.right)

#post order traversal of a tree
def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data ,end =" ")

#insert function
def insert(root,key):
    if root == None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

#dfs traversal
def level_order(root):
    if root == None:
        return
    q = [root]
    while q:
        node = q.pop(0)
        print(node.data,end = " ")
        if node.left:
            q.append(node.left)
        if node.right :
            q.append(node.right)

#min number in a tree
def min(root):
    if root.left == None:
        print(root.data)
    else:
        min(root.left)
            
#maxi sir code for max  
def maxi(root):
    temp = root
    while temp.right:
        temp = temp.right
    return temp.data

#max number in a tree
def max1(root):
    if root.right == None:
        print(root.data)      
    else:
        max1(root.right)


#prime numbers
def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count+=1
    if count ==2:
        return True
    else:
        return False

#countnodes
def countnodes(root):
    if root == None:
        return 0
    return 1 + countnodes(root.left)+countnodes(root.right)

#height of tree
def height(root):
    if root == None:
        return 0
    return 1+max(height(root.left),height(root.right))

#creating the tree
root =None
root = insert(root, 10)
insert(root, 5)
insert(root, 15)
insert(root, 3)
insert(root, 7)
insert(root, 12)
insert(root, 18)
print("\n inorder traversal of the tree is : ")
inorder(root)
print("\n preorder traversal of the tree is : ")
preorder(root)
print("\n postorder traversal of the tree is : ")
postorder(root)
print("\n level order traversal of the tree is : ")
level_order(root)
print("\n min : ")
min(root)
print("\n maximum : ")
max1(root)
print("\n max sir method : ",maxi(root))
print("\n prime numbers : ")
inorder_prime(root)
print("\nroot count : ")
print(countnodes(root))
print("\n height of tree : ",end =" ")
print(height(root))