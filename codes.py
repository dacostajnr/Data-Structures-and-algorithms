#  binary search allows you to quickly determine whether or not an element is in a list that is sorted 



def linear_search(L,target):
	'''
	List must alreaady be sorted

	1.Go through each index of the list
	2.compare the object at that index to the target
	'''
	for i in range(len(L)):
		if L[i]==target:
			return  True
		return False 


# solve for -1
def binary_search_iterative(L,target):
	low=0
	high=len(L)-1
	while (low<=high):		
		middle=(low+high)//2
		print(low,middle,high)			
		if target==L[middle]:
			return True
		elif target<L[middle]:
			high=middle-1
		else:
			low=middle+1
	return False
	

def binary_search_recursive(L,target,low,high):
	low = 0 
	high=len(L)-1
	middle=(low+high)//2
	if target==L[middle]:
		return True 
	if low>high:
		return False 
	elif target<L[middle]:
		#high=middle-1
		return binary_search_recursive(L[0:middle],target,low,high)
	else:
		#low =middle+1
		return binary_search_recursive(L[middle:],target,low,high)



def merge():
	pass

def mergeSort():
	pass


def quickSort():
	pass

def selectionSort():
	pass

def insertionSort():
	pass 



# run codes here
#print(binary_search_iterative([1,2,3,4,5,6],-1))
print(binary_search_recursive([1,2,3,4,5,6],2,0,5))    