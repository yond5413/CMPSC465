def heapify(arr, n, i): 
  
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2 
  
    
    if (l < n and arr[l] > arr[largest]): 
        largest = l 
  
   
    if (r < n and arr[r] > arr[largest]): 
        largest = r
      
    if (largest != i): 
        swap = arr[i] 
        arr[i] = arr[largest] 
        arr[largest] = swap; 

        heapify(arr, n, largest); 
  

def buildHeap(arr, n):     
    startIdx = int((n / 2)) - 1; 

    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i); 
  