def reverse(head, times):
    curr = head
    prev = None

    while times > 0 and curr:
        times -= 1
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


class Solution(object):
    def swapPairs(self, head):
        if head is None:
            return None

        left = head
        res = None
        prevleft = None
        size = 2

        while left and left.next:

            right = left
            for i in range(1):      # move to 2nd node of pair
                right = right.next

            nextleft = right.next

            # reverse current pair
            newhead = reverse(left, size)

            if prevleft:
                prevleft.next = newhead

            if res is None:
                res = newhead

            # after reversing, left becomes tail
            left.next = nextleft

            prevleft = left
            left = nextleft

        # odd node left at end
        if prevleft and left:
            prevleft.next = left

        return res if res else head