class Node:
    def __init__(self,name):
        self.name=name
        self.neighbors=[]
    def __str__(self):
        return self.name

class Graph:
    def __init__(self):
        self.node_list=[]
    def add_node(self,u):
        if ((isinstance(u,Node)) and (u not in self.node_list)):
            self.node_list.append(u)
            return True
        return False
    def add_neighbor(self,u,v):
        if ((isinstance(u,Node)) and (isinstance(v,Node)) and (u in self.node_list) and (v in self.node_list) and (u not in v.neighbors) and (v not in u.neighbors)):
            u.neighbors.append(v)
            v.neighbors.append(u)
            return True            
        return False
    def remove_node(self,u):
        if ((isinstance(u,Node)) and (u in self.node_list)):
            for i in u.neighbors:
                i.neighbors.remove(u)
            self.node_list.remove(u)
            return True
        return False

    def print_graph(self):
        for i in self.node_list:
            print("{}:{}".format(i.name,[j.name for j in i.neighbors]))

G=Graph()
A=Node("A")
B=Node("B")
C=Node("C")
G.add_node(A)
G.add_node(B)
G.add_neighbor(A,B)



        
