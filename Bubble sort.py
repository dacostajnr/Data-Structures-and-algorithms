def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i):
            # if back is bigger than front
            if array[j]>array[i]:
                #bring front to back
                x=array[j]
                array[j]=array[i]
                array[i]=x
    return array

print(bubbleSort([3,1,2,-9]))


