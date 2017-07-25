class Solution(object):
    def minSubArrayLen(self, s, nums):
        count, left, length = 0, 0, len(nums)+1
        for right, num in enumerate(nums):
            count += num
            while count >= s:
                length = min(length, right-left+1)
                count -= nums[left]
                left += 1
        return length if length <= len(nums) else 0