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
    print(root.data ,end =" ")
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
    while root:
        if root.left == None:
            print(root.data)
            return
            
        else:
            min(root.left)
            return
    

#max number in a tree
def max(root):
    while root:
        if root.right == None:
            print(root.data)
            return
            
        else:
            max(root.right)
            return

#creating the tree
root =None
root = insert(root, 10)
insert(root, 5)
insert(root, 15)
insert(root, 3)
insert(root, 7)
insert(root, 12)
insert(root, 18)
print("inorder traversal of the tree is :")
inorder(root)
print("\npreorder traversal of the tree is :")
preorder(root)
print("\npostorder traversal of the tree is :")
postorder(root)
print("\nlevel order traversal of the tree is :")
level_order(root)
print("\n min")
min(root)
print("\n max")
max(root)