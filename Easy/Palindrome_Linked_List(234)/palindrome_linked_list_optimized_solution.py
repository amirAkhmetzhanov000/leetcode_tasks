from utils import ListNode, transform_lists_into_linked

from typing import Optional

class Solution:
	@staticmethod
	def isPalindrome(head: Optional[ListNode]) -> bool:
		fast_pointer = head
		slow_pointer = head

		while fast_pointer and fast_pointer.next:
			fast_pointer = fast_pointer.next.next
			slow_pointer = slow_pointer.next

		current = slow_pointer
		prev = None

		while current:
			old_pointer = current.next
			current.next = prev
			prev = current
			current = old_pointer

		left, right = head, prev

		while right:
			if left.val != right.val:
				return False
			left = left.next
			right = right.next
		return True



def run_tests(solution_func):
    test_cases = [
        ("Четный палиндром", [1, 2, 2, 1], True),
        ("Нечетный палиндром", [1, 2, 3, 2, 1], True),
        ("Не палиндром", [1, 2, 3], False),
        ("Один элемент", [1], True),
        ("Пустой список", [], True),
        ("Два одинаковых", [1, 1], True),
        ("Два разных", [1, 2], False),
        ("Длинный палиндром", [1, 0, 1, 0, 1], True),
        ("Почти палиндром", [1, 2, 3, 1], False),
    ]

    for name, data, expected in test_cases:
        head = transform_lists_into_linked(data)
        result = solution_func(head)
        status = "✅ PASSED" if result == expected else "❌ FAILED"
        print(f"{status} | {name}: {data} (Ожидалось: {expected}, Получено: {result})")


head = transform_lists_into_linked([1,2,2,1])
solution = Solution()
run_tests(solution.isPalindrome)
