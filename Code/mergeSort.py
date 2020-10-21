
def divide(arr):
	if len(arr) >1:
		mid = len(arr) // 2
		l1 = arr[0:mid]
		l2 = arr[mid:len(arr)]
		s1 = divide(l1)
		s2 = divide(l2)
		return sort(s1, s2)
	else:
		return arr
	
def sort(list1, list2):
	result = []
	k = len(list1)
	g = len(list2)
	i = 0
	j = 0
	while i < k and j < g:
		if list1[i] < list2[j]:
			result.append(list1[i])
			i+=1
		else:
			result.append(list2[j])
			j+=1
	while i < k:
		result.append(list1[i])
		i+=1
	while j < g:
		result.append(list2[j])
		j+=1
	return result

def printList(arr):
	for i in range(len(arr)):
		print(arr[i],end=" ")
	
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	result = divide(arr)
	printList(result)
	
		
		
		