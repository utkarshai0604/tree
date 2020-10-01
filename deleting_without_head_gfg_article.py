
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 

# Function to initialize head 
	def __init__(self): 
		self.head = None
 
# Utility function to print the linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print (temp.data, )
			temp = temp.next

def delete(del_node):
	print("we are deleting node with value: ", del_node.data)
	temp=del_node.next
	
	del_node.data=temp.data	
	
	del_node.next.data=del_node.data
	
	del_node.next=temp.next


# Driver program 
llist = LinkedList() 
# creating a link list
llist.head = Node(50) 
llist.head.next = Node(20) 
llist.head.next.next = Node(15) 
llist.head.next.next.next = Node(4) 
llist.head.next.next.next.next = Node(10) 
llist.head.next.next.next.next.next = Node(12) 
# printing original linked list
llist.printList() 
val=llist.head.next.data
delete(llist.head.next)
print ("printing linked list after deleting ", val)
llist.printList() 
  
# code is contributed by Utkarsh Raj