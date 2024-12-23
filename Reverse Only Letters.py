class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        left=0
        right=len(s)-1
        liste=list(s)

        while left<=right:
            if liste[left].isalpha():
                if liste[right].isalpha():
                    liste[left],liste[right]=liste[right],liste[left]
                    left+=1
                    right-=1
                else:
                    right-=1
            else:
                left+=1
        return ''.join(liste)

        
