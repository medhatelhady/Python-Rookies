
def binary_search(arr, value, start, end ):

      while start <= end:
            mid = start + (end - start) // 2

            if arr[mid] == value:
                  return mid
            elif arr[mid]> value :
                  end = mid -1
            else:
                  start = mid +1
      return -1
