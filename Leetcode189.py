class Solution(object):
    def rotate(self, nums, k):
        temp1, temp2, l = [], [], len(nums)
        k = k%l
        for i in range(k):
            temp1.append(nums[l-k+i])
        for i in range(l-k):
            temp2.append(nums[i])
        for i in range(k):
            nums[i] = temp1[i]
        for i in range(l-k):
            nums[i+k] = temp2[i]