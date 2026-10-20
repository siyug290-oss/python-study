class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = {}
        for ch in s :
            if ch in count:
                count[ch] = count[ch] + 1
            else:
                count[ch] = 1

        for ch in t :
            if ch not in count:
                return False
            count[ch] = count[ch] - 1
            if count[ch] < 0:
                return False
        return True