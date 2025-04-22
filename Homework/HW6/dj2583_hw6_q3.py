
from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        if not orig_str:
            return

        last_char = None
        count = 0
        for char in orig_str:
            if self.data.is_empty():
                self.data.add_last((char, 1))
            elif char == self.data.trailer.prev.data[0]:
                curr_char, curr_count = self.data.trailer.prev.data
                self.data.trailer.prev.data = (curr_char, curr_count + 1)
            else:
                self.data.add_last((char, 1))

    def __add__(self, other):


        new_list = DoublyLinkedList()

        node = self.data.header.next
        while node is not self.data.trailer:
            new_list.add_last(node.data)
            node = node.next


        other_node = other.data.header.next
        if other_node is other.data.trailer:
            pass
        elif new_list.is_empty():
            while other_node is not other.data.trailer:
                new_list.add_last(other_node.data)
                other_node = other_node.next
        else:
            last_self_node = new_list.trailer.prev
            first_other_node = other_node

            if last_self_node.data[0] == first_other_node.data[0]:
                merged_char = last_self_node.data[0]
                merged_count = last_self_node.data[1] + first_other_node.data[1]
                last_self_node.data = (merged_char, merged_count)

                other_node = other_node.next

            while other_node is not other.data.trailer:
                new_list.add_last(other_node.data)
                other_node = other_node.next


        result = CompactString("")
        result.data = new_list
        return result

    def __lt__(self, other):

        self_node = self.data.header.next
        other_node = other.data.header.next
        self_remaining_count = 0
        other_remaining_count = 0

        while True:
            if self_remaining_count == 0 and self_node is not self.data.trailer:
                self_remaining_count = self_node.data[1]
            if other_remaining_count == 0 and other_node is not other.data.trailer:
                other_remaining_count = other_node.data[1]

            self_at_end = (self_node is self.data.trailer)
            other_at_end = (other_node is other.data.trailer)

            if self_at_end and other_at_end:
                return False
            if self_at_end:
                return True
            if other_at_end:
                return False

            self_char = self_node.data[0]
            other_char = other_node.data[0]

            if self_char != other_char:
                return ord(self_char) < ord(other_char)

            consume = min(self_remaining_count, other_remaining_count)
            self_remaining_count -= consume
            other_remaining_count -= consume

            if self_remaining_count == 0:
                self_node = self_node.next
            if other_remaining_count == 0:
                other_node = other_node.next

    def __eq__(self, other):
        self_node = self.data.header.next
        other_node = other.data.header.next

        while self_node is not self.data.trailer and other_node is not other.data.trailer:
            if self_node.data != other_node.data:
                return False
            self_node = self_node.next
            other_node = other_node.next

        return self_node is self.data.trailer and other_node is other.data.trailer
    def __le__(self, other):
        return self < other or self == other
    def __gt__(self, other):
        return not (self <= other)
    def __ge__(self, other):
        return not (self < other)

    def __repr__(self):
        string = ""
        for char, count in self.data:
            string += char * count
        return string



