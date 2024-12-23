class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        a=re.sub('[^A-Za-z0-9]+', '', s).lower()
        if a[::-1] == a:
            return True
        else:
            return False

        