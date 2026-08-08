class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare twin nodes
        first = head
        second = prev
        ans = 0

        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next

        return ans