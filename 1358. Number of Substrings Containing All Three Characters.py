'''1358. Number of Substrings Containing All Three Characters
Solved
Medium

Topics
Companies

Hint
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1




'''
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        characters= {'a':0, 'b':0, 'c':0}
        l=0
        total=0

        for r in range(len(s)):
            characters[s[r]]+=1

            while characters['a']>0 and characters['b']>0 and characters['c']>0:
                total+=len(s)-r
                characters[s[l]]-=1
                l+=1

        return total

        

        