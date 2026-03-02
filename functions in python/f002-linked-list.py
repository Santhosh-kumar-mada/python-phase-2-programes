#linked list
#create a linked list
class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None


#printg or traversal
def printnodes(head):
    cn = head
    while cn:
        print(cn.data,end="-->")
        cn=cn.next
    print("Null")
    
#deleting an element in linkedlist
def deletenode(head,ele):
    if head is None:
        return None
    if head.data==ele:
        return head.next
    cn = head
    while cn.next and cn.next.data!=ele:
        cn = cn.next
    
    if cn.next is None:
        return head
    
    #actual deleting command
    cn.next = cn.next.next

    return head


#create nodes
n1 = Node(20)
n2 = Node(30)
n3 = Node(50)
n4 = Node(40)

#linking
n1.next = n2
n2.next = n3
n3.next = n4


#printing call
printnodes(n1)
print("delete 20")
n1=deletenode(n1,20)
printnodes(n1)