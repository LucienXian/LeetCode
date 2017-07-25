class Solution(object):
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return nums
        f, l, i= nums[0], 0, 0
        while i!=len(nums)-1:
            if nums[i+1] != nums[i]+1:
                l = nums[i]
                s = str(f)
                if f == l:
                    res.append(s)
                else:
                    res.append(s+'->'+str(l))
                f = nums[i+1]
            i += 1
        l = nums[i]
        s = str(f)
        if f == l:
            res.append(s)
        else:
            res.append(s+'->'+str(l))
        return res