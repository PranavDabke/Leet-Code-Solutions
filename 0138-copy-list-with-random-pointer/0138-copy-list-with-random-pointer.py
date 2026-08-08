class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        old_to_new = {}

        # Create a new node for every original node
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Connect next and random pointers
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]