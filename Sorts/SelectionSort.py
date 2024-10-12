#Selection Sort
# It is comparison-based sorting algorithm
# It sorts array by selecting smallest (or largest) element from unsorted portion and swapping it with first unsorted element

def selectionsort(arr):
  min_idx=0
  for i in range(len(arr)):
    for j in range(len(arr)-1):
      if arr[i]<arr[j]:
         (arr[i],arr[j])=(arr[j],arr[i])
  return arr

mylist=[30,7,2,15,789,54]
print(mylist)
selectionsort(mylist)
print("Sorted List")
print(mylist)
