#bubble sort
# It compares and sorts the adjacent element if they are in incorrect order
# In the each pass, between each adjacent element, the max element goes to the end
# loop 1- i element through all n elements
# loop 2 - j element will starts from second last element, till ith element, with increments of -1 (travesing from right(max) to left(min)
# Time Complexity: O(n2)
# Auxiliary Space: O(1)

def bubblesort(arr):
  n=len(arr)

  for i in range(n):
    for j in range(n-1,i,-1):
      if arr[j]<arr[i]:
        (arr[i],arr[j])=(arr[j],arr[i])
  return arr

mylist=[30,7,2,15,789,54]
print(mylist)
bubblesort(mylist)
print("Sorted List")
print(mylist)
