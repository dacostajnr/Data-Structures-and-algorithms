def binary_search_iterative(array,target):
    # initialize min and max arrow point
    low=0
    high=len(array)-1
    # the two arrow points must not cross each other
    while (low<=high):
        middle=(high+low)//2
        # target is middle number
        if target==array[middle]:
            return True
        #target is smaller so reduce max arrow point
        elif target<array[middle]:
            high=middle-1
        # target is larger so increase min arrow point
        else:
            low=middle+1
    # arrow points crossed each other so target wasnt found            
    return False
        
print(binary_search_iterative([1,2,3,4,5,6],6))
