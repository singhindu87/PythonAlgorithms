# Insertion sort works by iteratively inserting each element of unsorted list into its correct position in a sorted portion of the list
# Assume - first element is always sorted
# in the first pass, compare 2nd element with 1st and replace if not in correct position
# in the second pass, compare with 1st and 2nd element and replace if not correct position
# Best case: O(n) , If the list is already sorted, where n is the number of elements in the list.
# store element in a variable
# pointer to search element in the second pass
# Average case: O(n 2 ) , If the list is randomly ordered
# Worst case: O(n 2 ) , If the list is in reverse order
# Auxiliary Space: O(1)

def insertionsort(arr):
  n=len(arr)
  for i in range(n):
    temp=arr[i] #temp will hold the value of element at ith position  
    pointer=i-1 #pointer will hold i-1th value
    while pointer>=0 and temp<arr[pointer]: #if  value at pointer is greater than temp element (in the first while, it will be adjacent left value. And, will keep on going left with decrement)
      arr[pointer+1]=arr[pointer] #right shift the pointer
      pointer-=1 #keep on repeating till pointer is at 0
    arr[pointer+1]=temp #assign the temp value to the correct position
  return arr

mylist=[30,7,2,15,789,54]
print(mylist)
insertionsort(mylist)
print("Sorted List")
print(mylist)
