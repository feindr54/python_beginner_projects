def MergeSort(arr, l,  r)
	if r > l:
    	Find the middle point to divide the array into two halves:  
    	m = int(l + (r-l) / 2)

     	MergeSort(arr, l, m)
     	MergeSort(arr, m+1, r)
     	merge(arr, l, m, r)



def merge(arr, l, m, r):
