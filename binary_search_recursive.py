def binary_search_recursive(array,target,low,high):
    if low>high:
        return False
    else:
        middle=(low+high)//2        
        if target==array[middle]:
            return True
        elif target<array[middle]:
            return binary_search_recursive(array,target,low,middle-1)
        else:
            return binary_search_recursive(array,target,middle+1,high)

data=[1,2,3,4,5,6]            
print(binary_search_recursive(data,2,0,len(data)-1))
