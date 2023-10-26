"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""

import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
            
        # sliding windows
        l = 0
        max_width = 1 # maximum window width
        chars = set() # set to keep current list of characters
        chars.add(s[0])
        
        for r in range(1, len(s)):
            if s[r] not in chars:
                chars.add(s[r]) # add unique char to set
                max_width = max(max_width, r-l+1) # extend window towards the right
            else:
                while s[l] != s[r]:
                    chars.remove(s[l]) # remove the left element until the left duplicate element is found
                    l += 1 # withdraw window from the left
                l += 1 # skip the duplicate element
                if len(s) - l + 1 <= max_width: # check if continue searching is necessary
                    return max_width
        return max_width
    
class Test(unittest.TestCase):
    def test_length_of_longest_substring(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(Solution().lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()