def moveElement(array, target):
    i = 0
    j = len(array) - 1

    while i < j:
        while i<j and array[j] == target:
            j -= 1
        if array[i] == target:
            array[i], array[j] = array[j], array[i]
        
        i += 1
    return array

array = [2,1,2,2,2,3,4,2]
target = 2
print(moveElement(array, target))
