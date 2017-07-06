class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = max(collections.Counter(tasks).values())
        max_ele = collections.Counter(tasks).values().count(count)
        return max(len(tasks), (count-1)*(n+1)+max_ele)
        