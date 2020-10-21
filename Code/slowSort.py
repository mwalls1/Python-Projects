def sort(arr):
	if len(arr) < 2:
		return arr
	i = 0
	while i < len(arr):
		j = i+1
		while j < len(arr):
			if arr[i] > arr[j]:
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
			j+=1
		i+=1
	return arr

def printList(arr):
		for i in range(len(arr)):
			print(arr[i], end=" ")
		print()
	
if __name__ == "__main__":
	arr = [12, 11, 13, 5, 6, 7]
	printList(sort(arr))
