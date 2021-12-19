
def remove_duplicates(arr):
      return list(set(arr))


def drop_duplicates(arr):


      i = 1
      while i < len(arr):
            if arr[i] == arr[i-1]:
                  del arr[i]
            else:
                  i += 1
      return arr

