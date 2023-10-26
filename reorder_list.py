"""
https://leetcode.com/problems/reorder-list/
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

from typing import Optional
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
            
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Solution:
        find the midde of the linked list by using slow and fast pointer
        reverse the second part of the linked list
        """
            
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        curr, prev = slow.next, None
        slow.next = None # set the next of the slow to None to break the link
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev
        
        # Step 3: Merge the first half and the reversed second half of the linked list
        first_half = head
        while first_half and second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2
        
        
class Test(unittest.TestCase):
    
    def test_reorder_list(self):
        node = ListNode(val=1, next = ListNode(val=2, next = ListNode(val=3, next = ListNode(val=4))))
        Solution().reorderList(node)
        self.assertEqual(node.val, 1)
        self.assertEqual(node.next.val, 4)
        self.assertEqual(node.next.next.val, 2)
        self.assertEqual(node.next.next.next.val, 3)
        
if __name__ == "__main__":
    unittest.main()