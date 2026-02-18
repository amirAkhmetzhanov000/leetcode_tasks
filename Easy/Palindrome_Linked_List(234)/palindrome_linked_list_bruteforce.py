from typing import Optional

from utils import ListNode, transform_lists_into_linked

class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		if head:
			current = head
			prev = None
			future_pointer = None

			while True:
				temp_val = current.next
				if temp_val is not None:
					future_pointer = current.next.next


				if future_pointer is None:
					if prev is not None:
						mid_left = prev
						mid_right = current
					else:
						mid_left = current
						mid_right = current.next

					while mid_right is not None and mid_left is not None:
						if mid_right.val != mid_left.val:
							return False
						mid_right = mid_right.next
						mid_left = mid_left.next
					return True

				current.next = prev
				prev = current
				current = temp_val

		return False





head = [1,2,1]
linked_head = transform_lists_into_linked(head)
solution = Solution()

result = solution.isPalindrome(linked_head)
print(result)