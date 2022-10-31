def linear_search(list, target):
  "Returns the index position of the target if found, else returns None"
  for item in range(0, len(list)):
    if list[item] == target:
      return item
  return None


def verify(index):
  "Verifies if the index exits"
  if index is not None:
    print("Target found at index ", index)
  else:
    print("Target not found.")


numbers = [num for num in range(1, 20)]

result_1 = linear_search(numbers,  12)
result_2 = linear_search(numbers,  25)

verify(result_1)
verify(result_2)