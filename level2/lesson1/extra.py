import main


def sum_linked_lists(list_a, list_b):
    sum_list = main.LinkedList()

    if list_a.len() == list_b.len():
        node_a = list_a.head
        node_b = list_b.head
        while node_a is not None:
            sum_list.add_in_tail(main.Node(node_a.value + node_b.value))
            node_a = node_a.next
            node_b = node_b.next

    return sum_list
