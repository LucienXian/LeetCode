class Solution(object):
    def twoSum(self, numbers, target):
        res = []
        left, right = 0, len(numbers)-1
        while left<right:
            total = numbers[left]+numbers[right]
            if total==target:
                res.append(left+1)
                res.append(right+1)
                break
            elif total < target:
                left += 1
            else:
                right -= 1
        return res