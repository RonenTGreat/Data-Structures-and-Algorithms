You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

**Problem Source:**  [LeetCode](https://leetcode.com/problems/sort-the-people/)

```python
test_1 = Solution()
test_1.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170])
# ["Mary","Emma","John"]

test_2 = Solution()
test_2.sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150])
# ["Bob","Alice","Bob"]
```
