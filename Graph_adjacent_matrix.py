class Node:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name


class Graph:
    def __init__(self):
        self.node_list=[]
        self.node_indices={}
    def add_node(self,u):
        if (isinstance(u,Node) and (u.name not in self.node_indices.keys())):
            # check if this is the first node
            if (len(self.node_list)==0):
                self.node_list.append([0])
                self.node_indices[u.name]=0
                
                return True
            # this is not the first node
            for i in self.node_list:
                i.append(0)
            self.node_list.append([0]*(len(self.node_list)+1))
            self.node_indices[u.name]=len(self.node_indices)
            return True            
        return False
    def remove_node(self,u):
        if (isinstance(u,Node) and (u.name in self.node_indices.keys())):
            # get position
            position=self.node_indices[u.name]
            # remove main list
            del self.node_list[position]
            # remove from all ends
            for i in self.node_list:
                del i[position]
            # update dictionary
            for k,v in self.node_indices.items():
                if v>position:
                    self.node_indices[k]=v-1
            del self.node_indices[u.name]
            return True
        return False
    def add_edge(self,u,v,cost=1):
        if (isinstance(u,Node) and isinstance(v,Node) and (u.name in self.node_indices.keys()) and (v.name in self.node_indices.keys())):
            # get position of u
            u_position=self.node_indices[u.name]
            # get position of v
            v_position=self.node_indices[v.name]
            # update the list of u
            self.node_list[u_position][v_position]=cost
            self.node_list[v_position][u_position]=cost
            return True
        return False
    def print_graph(self):
        for i in self.node_list:
            print(i)
            print("\n")

G=Graph()
A=Node("A")
B=Node("B")
G.add_node(A)
G.add_node(B)
