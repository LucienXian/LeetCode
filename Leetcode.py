class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        result, start, end = 0, arrays[0][0], arrays[0][-1]
        for i in xrange(1, len(arrays)):
            result = max(result, abs(arrays[i][0]-end))
            result = max(result, abs(arrays[i][-1]-start))
            start = min(arrays[i][0], start)
            end = max(arrays[i][-1], end)
        return result