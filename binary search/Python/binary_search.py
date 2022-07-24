def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while first <= last:
    mid_point = (first + last) // 2

    if list[mid_point] == target:
      return mid_point
    elif list[mid_point] < target:
      first = mid_point + 1
    else:
      last = mid_point - 1
  return None


def verify(index):
  "Verifies if the index exits"
  if index is not None:
    print("Target found at index ", index)
  else:
    print("Target not found.")


numbers = [num for num in range(1, 21)]

result_1 = binary_search(numbers, 5)
result_2 = binary_search(numbers,  25)

verify(result_1)
verify(result_2)
