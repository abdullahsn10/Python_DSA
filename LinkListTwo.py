class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



head = ListNode(10, None)
second = ListNode(20, None)
third = ListNode(30, None)
fourth = ListNode(40, None)
head.next = second
second.next = third
third.next = fourth


def print_list(head:ListNode):
    if head is None:
        print("Empty List")
    
    itr:ListNode = head
    llstr = ''

    while itr:
        llstr += f'{itr.val} --> '
        itr = itr.next

    print(llstr)

print_list(head)