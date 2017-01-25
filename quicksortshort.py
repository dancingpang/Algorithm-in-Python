# Quicksort algorithm implemented in Python. Also counts the total number of comparisons used to sort the given input file 
fh = open("....txt")

list = []

for line in fh:
    line =line.strip()
    line = int(line)
    list.append(line)

def quicksort(alist):
    count = 0
    left = []
    right = []
    if len(alist) <=1:
        return alist, 0
    else:
        pivot = alist[0]
        for x in alist[1:]:
            if x < pivot:
                left.append(x)
            if x >= pivot:
                right.append(x)
            count += 1          
    
    part1, count1 = quicksort(left)
    part2, count2 = quicksort(right)
    
    return (part1 + [pivot] + part2), (count + count1 + count2)
    
print (quicksort(list))
     