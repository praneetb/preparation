# Given an array of integers, return indices of the two numbers such that
# they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}

        for idx in range(len(nums)):
          complement = target - nums[idx]

          if complement in map.values():
            return [map.values().index(complement), idx]

          map[idx] = nums[idx]

        return[]


def main():
  nums = [2, 7, 11, 15, 4]
  target = 15

  sol = Solution()
  res = sol.twoSum(nums, target)

  print res

if __name__ == '__main__':
  main()
