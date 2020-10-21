def sort(arr):
	if len(arr) < 2:
		return arr
	sorted = False
	while sorted == False:
		numSwaps = 0
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
				numSwaps+=1
		if numSwaps == 0:
			sorted = True
	return arr
	
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")

if __name__ == "__main__":
	arr = [12,13,1,7,6,5]
	printList(sort(arr))