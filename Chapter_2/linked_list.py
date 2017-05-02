

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


def delete_node(head, data):

    current = head

    if current.data == data:
        return current.next

    while current.next:
        if current.next.data == data:
            current.next = current.next.next
            return head
        else:
            current = current.next

    return head


if __name__ == '__main__':

    ll = Node(1)
    ll.append_to_tail(2)
    ll.append_to_tail(3)
    ll.append_to_tail(4)
    ll.append_to_tail(5)
    ll.print()
    ll = delete_node(ll, 3)
    ll.print()

