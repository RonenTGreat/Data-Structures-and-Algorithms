from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last_index_of_nums1 = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last_index_of_nums1] = nums1[m - 1]
                m -= 1
            else:
                nums1[last_index_of_nums1] = nums2[n - 1]
                n -= 1
            last_index_of_nums1 -= 1

        while n > 0:
            nums1[last_index_of_nums1] = nums2[n - 1]
            n, last_index_of_nums1 = n - 1, last_index_of_nums1 - 1

