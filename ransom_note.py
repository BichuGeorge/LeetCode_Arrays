"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


First we will create a dictionary to count the occurrences of each character in the ransom note.
Then we will iterate through the characters in the ransom note and check if each character exists in the magazine with enough occurrences.
Then we will return true if all characters in the ransom note can be found in the magazine with sufficient counts, otherwise false.
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_count = {}
        flag = True
        if len(magazine) == 0:
            return False
        for ch in ransomNote:
            if ch in ransom_count:
                ransom_count[ch]+=1
            else:
                ransom_count[ch] = 1
        for key, value in ransom_count.items():
            if key in magazine:
                if magazine.count(key) >= value:
                    continue
                else:
                    flag = False
            else:
                return False
        return flag
            