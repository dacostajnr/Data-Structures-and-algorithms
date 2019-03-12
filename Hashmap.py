class Hashmap:
    def __init__(self):
        self.length=64
        self.list=[]
        for i in range(self.length):
            self.list.append([])
    def _hash(self,key):
        hashed=0
        for i in key:
            hashed+=ord(i)
        return hashed
    
    def add(self,key,value):
        # get the ascii of key
        ascii=self._hash(key)
        # get the position in the main_list
        position=ascii%len(self.list)
        # loop through each element and check for collision
        for i in self.list[position]:
            if i[0]=="key":
                i[1]=value
                return True
        self.list[position].append([key,value])
        
    def get(self,key):
        # get ascii
        ascii=self._hash(key)
        # get position
        position=ascii%len(self.list)        
        # check if it exists
        for i in self.list[position]:
            if i[0]==key:
                return i[1]
        # return false
        return False
    
    def remove(self,key):
        # get ascii
        ascii=self._hash(key)
        # get position
        position=ascii%len(self.list)
        # check if it exists
        for i in self.list[position]:
            if i[0]==key:
                self.list[position].remove(i)
                return True
        return False





H=Hashmap()
H.add("a",1)
H.add("b",2)
        
        
