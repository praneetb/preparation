# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their
# nodes contain a single digit. Add the two numbers and return it as a
# linked list.
#You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None and l2 == None:
          print "Empty Linked lists!!!"
          return None

        carry = 0
        l3 = ListNode(0)
        tmp1 = l3
        while l1 or l2 or carry != 0:
          val1 = val2 = 0

          if l1:
            val1 = l1.val
            l1 = l1.next
          if l2:
            val2 = l2.val
            l2 = l2.next

          sum = val1+val2+carry
          #if sum == 0:
          #  break

          carry = sum/10
          tmp1.next = ListNode(sum%10)
          tmp1 = tmp1.next

        return l3.next


def main():
  l1 = ListNode(0)
  l1.next = ListNode(4)
  #l1.next.next = ListNode(3)

  l2 = ListNode(0)
  l2.next = ListNode(6)
  l2.next.next = ListNode(9)

  sol = Solution()
  l3 = sol.addTwoNumbers(l1, l2)
  while l3:
    print l3.val
    l3 = l3.next

if __name__ == '__main__':
  main()
