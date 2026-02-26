from typing import Optional

from utils import ListNode, transform_lists_into_linked, linked_to_list

class Solution:
	def mergeTwoLists(
		self,
		list1: Optional[ListNode],
		list2: Optional[ListNode]
	) -> Optional[ListNode]:
		dummy = ListNode()
		head = dummy

		while True:
			if list1:
				dummy.next = ListNode(val=list1.val, next=list1.next)
				dummy = dummy.next
				list1 = list1.next

			if list2:
				dummy.next = ListNode(val=list2.val, next=list2.next)
				dummy = dummy.next
				list2 = list2.next

			if dummy.next == None:
				break

		if head:
			dummy_2 = head
			head_2 = dummy_2
			while dummy_2 and dummy_2.next:
				if dummy_2.val > dummy_2.next.val:
					old_value = dummy_2.val
					dummy_2.val = dummy_2.next.val
					dummy_2.next.val = old_value
					dummy_2 = dummy_2.next
					continue
				dummy_2 = dummy_2.next
			return head_2.next

		return None


solution = Solution()

list1 = [1,2]
list2 = [5,4,2,5,6,7]


linked_list_1 = transform_lists_into_linked(list1)
linked_list_2 = transform_lists_into_linked(list2)

result = solution.mergeTwoLists(linked_list_1, linked_list_2)

def run_tests(sol_class):
	solver = sol_class()

	test_data = [
		([1, 2, 4], [1, 3, 4], "Стандартный случай"),
		([], [], "Оба пустые"),
		([], [0], "Один пустой"),
		([1, 2], [3, 4, 5, 6], "Разная длина"),
		([1, 10, 100], [2, 20], "Непересекающиеся значения"),
		([-9,3], [5,7], "Отрицательные значения на старте"),
	]

	for l1_raw, l2_raw, name in test_data:
		l1 = transform_lists_into_linked(l1_raw)
		l2 = transform_lists_into_linked(l2_raw)

		merged = solver.mergeTwoLists(l1, l2)

		print(f"Тест: {name}")
		print(f"  Вход: {l1_raw} + {l2_raw}")
		print(f"  Выход: {linked_to_list(merged)}")
		print("-" * 30)


run_tests(Solution)