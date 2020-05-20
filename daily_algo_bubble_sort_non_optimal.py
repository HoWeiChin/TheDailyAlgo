def bubble_sort(arr):

    #always increase latest_sort_boundary (LSB) by 1.
    #because in our case here, we push the maximum element to the left
    #for each run of the outer loop
    
    for latest_sort_boundary in range(len(arr)):
        
        for scanner in range(len(arr)-1, latest_sort_boundary, -1):
            
            if arr[scanner] > arr[scanner-1]:
                arr[scanner], arr[scanner-1] = arr[scanner-1], arr[scanner]

    return arr
