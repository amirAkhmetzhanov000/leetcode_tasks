def add_underscores_to_title(title: str) -> str:
    code_number, code_title = title.split('.')
    return '{code_title}_{code_number}'.format(
        code_title='_'.join(code_title.split(' ')).lstrip('_'),
        code_number=code_number
    )


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def transform_lists_into_linked(non_linked_list: list):
    if not non_linked_list:
        return

    head = ListNode(non_linked_list[0])
    current = head

    for number in non_linked_list[1:]:
        current.next = ListNode(number)
        current = current.next

    return head


def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def iterate_over_linked_list(linked_list):
    current = linked_list
    while current:
        print(current.val)
        current = current.next
