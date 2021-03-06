

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, data):

        current = self

        while current.next:
            current = current.next

        current.next = Node(data)

    def print(self):

        current = self
        print('[', end='')

        while current.next:
            print(current.data, end=', ')
            current = current.next

        print(current.data, end=']\n')


def del_dups(head):

    seen = [head.data]
    current = head

    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.append(current.next.data)
            current = current.next

    return head


if __name__ == '__main__':

    ll = Node(1)
    ll.append_to_tail(2)
    ll.append_to_tail(3)
    ll.append_to_tail(2)
    ll.append_to_tail(4)
    ll.print()
    ll = del_dups(ll)
    ll.print()

