class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                # Step 2: Find start of cycle
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None