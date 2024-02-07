import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Previous Node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            if current.next is not None:
                print(f"{current.data} -> ", end="")
            else:
                print(current.data)
            current = current.next

    # adding reverse method
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # adding sort method
    def sort_list(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None

        current = self.head
        while current is not None:
            next_node = current.next

            sorted_list = self.sorted_insert(sorted_list, current)

            current = next_node

        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            sorted_list = new_node
        else:
            current = sorted_list
            while current.next is not None and current.next.data < new_node.data:
                current = current.next

            new_node.next = current.next
            current.next = new_node

        return sorted_list


# merge two sorted lists
def merge_sorted_lists(list1, list2):

    merged_list = LinkedList()

    current_1 = list1.head
    current_2 = list2.head

    while current_1 is not None and current_2 is not None:
        if current_1.data <= current_2.data:
            merged_list.insert_at_end(current_1.data)
            current_1 = current_1.next
        else:
            merged_list.insert_at_end(current_2.data)
            current_2 = current_2.next

    while current_1 is not None:
        merged_list.insert_at_end(current_1.data)
        current_1 = current_1.next

    while current_2 is not None:
        merged_list.insert_at_end(current_2.data)
        current_2 = current_2.next

    return merged_list


def main():
    # creating two linked lists
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    # filling the lists
    for _ in range(10):
        llist_1.insert_at_end(random.randint(0, 100))
        llist_2.insert_at_end(random.randint(0, 100))

    print("printing first list:")
    llist_1.print_list()
    print("printing second list:")
    llist_2.print_list()

    # sorting the lists
    llist_1.sort_list()
    llist_2.sort_list()

    merged_list = merge_sorted_lists(llist_1, llist_2)

    print("printing merged list:")
    merged_list.print_list()


if __name__ == "__main__":
    main()
