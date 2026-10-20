class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lst = set()
        for i in nums:
            if i in lst:
                return True
            lst.add(i)
        return False



