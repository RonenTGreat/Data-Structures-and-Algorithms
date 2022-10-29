def resursive_binary_search(list, target):
  if len(list) == 0:
    return False
  
  else:
    midpoint = len(list) // 2
    if list[midpoint] == target:
      return True
    else:
      if list[midpoint] < target:
        return resursive_binary_search(list[midpoint + 1:], target)
      else:
        return resursive_binary_search(list[:midpoint], target)

def verify(result):
  print("Target found: ", result)


numbers = [num for num in range(1, 21)]

result_1 = resursive_binary_search(numbers, 5)
result_2 = resursive_binary_search(numbers,  25)

verify(result_1)
verify(result_2)
