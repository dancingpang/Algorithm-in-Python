def mergesort(a):
    # returns sorted_list and inversion_count
    n = len(a)
    if n <= 1:
        return a, 0
    else:
        L = a[:n//2]
        R = a[n//2:]
    
    L, left_inversions = mergesort(L)
    R, right_inversions = mergesort(R)
    
    sorted_list, merge_count = merge(L, R)
    
    return sorted_list, (merge_count + left_inversions + right_inversions)
    
    
def merge(a, b):
    # returns merged a+b, inversion_count for elements in a, b
    # preconditions: a is a sorted list; b is a sorted list
    
    result = []
    
    i = 0
    j = 0
    count = 0
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
            
        else:
            result.append(b[j])
            j += 1
            count += len(a) - i
            
    result = result + a[i:] + b[j:]
    return result, count
    

