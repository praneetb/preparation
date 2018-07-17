#
# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int, substring
    """
    ret_list = []
    for i in range(len(s)):
      tmp_list = []
      tmp_list.append(s[i])
      for j in range(i+1, len(s)):
        if s[j] in tmp_list:
          break
        tmp_list.append(s[j])
      if len(tmp_list) > len(ret_list):
        ret_list = tmp_list

    return len(ret_list), ret_list

def main():
  sol = Solution()
  print(sol.lengthOfLongestSubstring("abcabcebb"))
  print(sol.lengthOfLongestSubstring("bbbb"))
  print(sol.lengthOfLongestSubstring("pwwkew"))

if __name__ == '__main__':
  main()

