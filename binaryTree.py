class Node:
    def __init__(self,val):
        self.val=val
        self.left_child=None
        self.right_child=None
                
    def insert(self,data):
        if self.val==data:
            return False
        # look at the left
        elif data<self.val:
            # node has a left child
            if self.left_child:
                return self.left_child.insert(data)                
            # node has no left child
            else:
                self.left_child=Node(data)
                return True                        
        else:
            # look at the right
            if self.right_child:
                # node has a right child
                return self.right_child.insert(data)                
            else:
                # node has no right child
                self.right_child=Node(data)
                return True
                

    # LMR
    # Smallest to biggest
    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.val)
        if self.right_child:
            self.right_child.inorder()

    #MLR
    def pre_order(self):
        print(self.val)
        if self.left_child:
            self.left_child.pre_order()        
        if self.right_child:
            self.right_child.pre_order()
    #LRM
    def post_order(self):        
        if self.left_child:
            self.left_child.post_order()        
        if self.right_child:
            self.right_child.post_order()
        print(self.val)

    def find(self,data):
        # if val is equal to node
        if self.val==data:
            return True
        
        elif data<self.val:
            # data is smaller than current node.Look left 
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            # data is bigger than current node.Look right
            if self.right_child:
                return self.right_child.find(data)
            else:
                return  False
    def getHeight(self):
        # node has both right and left children
        if (self.right_child and self.left_child):
            return 1+max(self.right_child.getHeight(),self.left_child.getHeight())
        # node has right child only
        elif self.right_child:
            return 1+self.right_child.getHeight()
        # node has left child only
        elif self.left_child:
            return 1+self.left_child.getHeight()
        # node has no child
        else:
            return 1
    def getSize(self):
        if (self.left_child and self.right_child):
            return 1+self.right_child.getSize()+self.left_child.getSize()
        elif (self.left_child):
            return 1+self.left_child.getSize()
        elif (self.right_child):
            return 1+self.right_child.getSize()
        else:
            return 1

    def remove(self,data):
        # get the Node
        #node=Node
        pass
class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root:
            # added return
            return self.root.insert(data)
        else:
            self.root=Node(data)
            # shifted return to right
            return  True
         
        

    def inorder(self):
        if self.root:
             self.root.inorder()
        else:
            return False
    def post_order(self):
        if self.root:
            return self.root.post_order()
        return False
    def pre_order(self):
        if self.root:
            return self.root.pre_order()
        return False
    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getHeight(self):
        # to get the height of the tree
        # start at root node
        # 1+ maximum of the height of its children
        # if the current node has no left child
            #return 1
        # if the current node has no right child
            # return 1
        if self.root:
            return self.root.getHeight()
        else:
            return 0
    def getSize(self):
        # get size returns the total number of nodes in the tree
        # start at root node
        # 1+size of children
        # if the current node has no left child
            # return 1
        # if the current node has no right child
            # return 1
        if self.root:
            return self.root.getSize()
        else:
            return 0
    def remove(self,data):
        if self.root:
            if self.find(data):
                return self.root.remove(data)
            else:
                return False
        else:
            return False
        
    


T=Tree()
print(T.insert(30))
print(T.find(30))
print(T.insert(15))
T.insert(45)
T.insert(4)
T.insert(31)
T.insert(90)
T.insert(20)
T.insert(21)
T.insert(19)

T.inorder()

T.getHeight()
