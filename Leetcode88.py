class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0
        nums1[:], nums2[:] = nums1[:m], nums2[:n]
        temp = []
        while j < n and i < m:
            if nums1[i]>nums2[j]:
                temp.append(nums2[j])
                j += 1
            else:
                temp.append(nums1[i])
                i += 1
        if i != m:
            temp += nums1[i:]
        if j != n:
            temp += nums2[j:]
        nums1[0:] = temp