class Node:
    def __init__(self,data,_next=None):
        self.data=data
        self.next=_next
    def add(self):
        # check if current node has a next node


class LinkedList:
    def __init__(self):
        self.root=None

    def add(self,data):
        if self.root:
            # there already exists a root node

            # get the root node
            root_node=self.root
            # get the new node
            
        else:
            #this is the first node
            new_node=Node(data)
            self.root=new_node 
        
        
