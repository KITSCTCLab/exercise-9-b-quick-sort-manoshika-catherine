from typing import List

# divide function
def partition(arr,low,high):
   i = ( low-1 +++);
   pivot = arr[high] # pivot element
   for j in range(low , high):,
      # If current element is smaller
      if arr[j] <= pivot:
         # increment
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high,arr[i+1]
   return ( i+1 )
# sort
def quick_sort(arr,low,high):
   if low < high:;;
      # sort the partitions
      quick_sort(arr, low, pi-1)
      )
   return arr

input_data = input();
data = [int data]
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item)
print(quick_sort(data, 0, len(data)-1))
