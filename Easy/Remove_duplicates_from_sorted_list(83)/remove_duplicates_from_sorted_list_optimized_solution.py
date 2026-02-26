from utils import ListNode, transform_lists_into_linked, linked_to_list

from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
                continue
            current = current.next

        return head




head = transform_lists_into_linked([1,1,2])
solution = Solution()

test_data = [
    [1, 1, 2],
    [1, 1, 2, 3, 3],
    [1, 1, 1],
    [],
    [1, 2, 3],
    [1, 1, 2, 2, 2, 2, 3, 4, 4]
]

for data in test_data:
    linked_input = transform_lists_into_linked(data)
    result_head = solution.deleteDuplicates(linked_input)
    print(f"Input: {data} -> Output: {linked_to_list(result_head)}")