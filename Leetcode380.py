class RandomizedSet(object):

    def __init__(self):
        self.nums, self.pos = [], {}
        """
        Initialize your data structure here.
        """
        

    def insert(self, val):
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums)-1
        return True
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        

    def remove(self, val):
        if val not in self.pos:
            return False
        index, last = self.pos[val], self.nums[-1]
        self.nums[index] = last
        self.pos[last] = index
        self.nums.pop()
        self.pos.pop(val)
        return True
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]
        """
        Get a random element from the set.
        :rtype: int
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()