class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        majority = nums[0]
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == majority:
                count = count + 1
            else:
                count = count - 1
                if count == 0:
                    majority = nums[i]
                    count = 1
        return majority
