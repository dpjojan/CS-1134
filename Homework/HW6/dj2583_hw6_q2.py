from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        if not num_str or not num_str.strip():
            raise ValueError("Need an input")

        significant_digits_str = num_str.lstrip('0')
        if not significant_digits_str:
            significant_digits_str = '0'

        for digit_char in significant_digits_str:
            if not digit_char.isdigit():
                raise ValueError("Need a valid number")
            self.data.add_last(int(digit_char))

    def __add__(self, other):
        total = DoublyLinkedList()
        runover = 0

        node1 = self.data.trailer.prev
        node2 = other.data.trailer.prev

        while node1 != self.data.header or node2 != other.data.header:
            digit1 = node1.data if node1 != self.data.header else 0
            digit2 = node2.data if node2 != other.data.header else 0

            summed = digit1 + digit2 + runover
            total.add_first(summed % 10)
            runover = summed // 10

            if node1 != self.data.header:
                node1 = node1.prev
            if node2 != other.data.header:
                node2 = node2.prev

        if runover:
            total.add_first(runover)


        result = Integer("0")
        if total.is_empty():
             result.data.add_first(0)
        else:

            if not result.data.is_empty() and result.data.header.next != result.data.trailer:
                 result.data.delete_node(result.data.header.next)
            result.data = total

        return result

    def __mul__(self, other):
        if str(self) == "0" or str(other) == "0":
            return Integer("0")

        final_total = Integer("0")
        shift_zeros = 0

        multiplier_node = other.data.trailer.prev
        while multiplier_node != other.data.header:
            multiplier_digit = multiplier_node.data
            partial_product = DoublyLinkedList()
            carry = 0

            multiplicand_node = self.data.trailer.prev
            while multiplicand_node != self.data.header or carry:
                multiplicand_digit = multiplicand_node.data if multiplicand_node != self.data.header else 0
                product = multiplicand_digit * multiplier_digit + carry
                partial_product.add_first(product % 10)
                carry = product // 10
                if multiplicand_node != self.data.header:
                    multiplicand_node = multiplicand_node.prev

            for i in range(shift_zeros):
                partial_product.add_last(0)

            partial_product_integer = Integer("0")
            if not partial_product.is_empty():
                partial_product_integer.data = partial_product

            final_total = final_total + partial_product_integer

            shift_zeros += 1
            multiplier_node = multiplier_node.prev

        return final_total

    def __repr__(self):
        if self.data.is_empty():
             return "0"
        string = ''
        current = self.data.header.next
        while current != self.data.trailer:
            string += str(current.data)
            current = current.next
        return string if string else "0"

