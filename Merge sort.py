def merge(left,right):
    i,j=0,0
    result=[]
    # merging must go on and on
    while (i<len(left) and j<len(right)):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while(i<len(left)):
        result.append(left[i])
        i+=1
    while (j<len(right)):
        result.append(right[j])
        j+=1
    return result


def mergeSort(array):
    middle=len(array)//2
    if len(array)<2:
        return array
    left = mergeSort(array[0:middle])
    right=mergeSort(array[middle:])
    return merge(left,right)

print(mergeSort([3,2,1,0,12]))
    
