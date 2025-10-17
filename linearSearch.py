def linearSearch(arr,targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

arr = [3,5,2,8,4,9]
targetVal=4

result=linearSearch(arr,targetVal)

if result != -1:
    print(f"value {targetVal} found at index {result}")
else:
    print(f"value {targetVal} not found")