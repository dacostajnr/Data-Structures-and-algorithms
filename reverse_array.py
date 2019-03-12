def reverse_array(array):
    for i in range(len(array)//2):
        # get the back item
        back_item=array[i]
        # get the front item
        front_item=array[len(array)-1-i]
        # swap them
        array[i],array[len(array)-1-i]=front_item,back_item
    return array

print(reverse_array([1,2,3,4,5]))
