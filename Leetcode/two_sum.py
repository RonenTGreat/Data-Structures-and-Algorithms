from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1 in range(0, len(nums)):
            for index_2 in range(index_1 + 1, len(nums)):
                if nums[index_1] + nums[index_2] == target:
                    return [index_1, index_2]



test_1 = Solution()
print(test_1.twoSum([2, 7, 11, 15], 9))

test_2 = Solution()
print(test_2.twoSum([3, 2, 4], 6))

test_3 = Solution()
print(test_3.twoSum([3, 3], 6))

test_4 = Solution()
print(test_4.twoSum([2, 5, 5, 4], 10))

