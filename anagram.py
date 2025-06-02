"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


If the lengths of the two strings are not equal, they cannot be anagrams. Return false immediately.
If every character appears the same number of times in both strings, they are anagrams
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count_hash_s = {}
        count_hash_t = {}
        for c in s:
            if c in count_hash_s:
                count_hash_s[c] += 1
            else:
                count_hash_s[c] = 0
        for c in t:
            if c in count_hash_t:
                count_hash_t[c] += 1
            else:
                count_hash_t[c] = 0
        for i_s in s:
            if i_s not in t:
                return False
            elif count_hash_s[i_s] != count_hash_t[i_s]:
                return False
        return True
        
        