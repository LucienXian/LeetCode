def moveZeroes(self, nums):
        count = 0
        for num in nums:
            if num==0:
                count += 1
        i = 0
        for num in nums:
            if num!=0:
                nums[i] = num
                i += 1
        while i<len(nums):
            nums[i] = 0
            i += 1