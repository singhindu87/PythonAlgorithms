# Binary Search (BST)
# Searching in BST is assumed to be a sorted list
# first, variables are defined based on the length of array
# secondly, through a while loop, comparing first to be lesser or equal to last element, mid variable is calculated
# when mid is compared with serached element on following conditions
# if item is greater than value at the mid of array, then the first element position is moved to mid +1
# if item is less than value at the mid of the array, then the last element position is moved to mid -1
# if the item is at mid of array, then item is returned
# else false or -1 is returned

def binary_search(arr,item):
  first=0
  last=len(arr)-1
  while first<=last:
    mid=first + ((last-first)//2)
    if arr[mid]<item:
      first=mid+1
    elif arr[mid]>item:
      last=mid-1
    else:
      return item
    return -1
    
    

mylist=[1,2,9,40,55]

binary_search(mylist,9)
binary_search(mylist,4)

