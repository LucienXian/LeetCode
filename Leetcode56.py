class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        if not intervals:
            return ans
        after_sort = sorted(intervals, key = lambda x: x.start)
        start, end = after_sort[0].start, after_sort[0].end
        for i in after_sort[1:]:
            if i.start > end:
                ans.append(Interval(start, end))
                start, end = i.start, i.end
            else:
                end = max(end, i.end)
        ans.append(Interval(start, end))
        return ans