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
    def reverseKGroup(self, head, k):

        if head is None or k == 1:
            return head

        left = head
        res = None
        prevleft = None

        while left:

            right = left

            count = 1
            while count < k and right:
                right = right.next
                count += 1

            if right is None:
                if prevleft:
                    prevleft.next = left
                break

            nextleft = right.next

            newhead = reverse(left, k)

            if prevleft:
                prevleft.next = newhead

            if res is None:
                res = newhead

            left.next = nextleft

            prevleft = left
            left = nextleft

        return res if res else head