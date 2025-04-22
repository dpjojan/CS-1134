from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    merged_list = DoublyLinkedList()
    def merge_sublists(node1, node2):
        if node1 is srt_lnk_lst1.trailer:
            current = node2
            while current is not srt_lnk_lst2.trailer:
                merged_list.add_last(current.data)
                current = current.next
            return

        if node2 is srt_lnk_lst2.trailer:
            current = node1
            while current is not srt_lnk_lst1.trailer:
                merged_list.add_last(current.data)
                current = current.next
            return

        if node1.data <= node2.data:
            merged_list.add_last(node1.data)
            merge_sublists(node1.next, node2)
        else:
            merged_list.add_last(node2.data)
            merge_sublists(node1, node2.next)

    first_node1 = srt_lnk_lst1.header.next
    first_node2 = srt_lnk_lst2.header.next

    merge_sublists(first_node1, first_node2)

    return merged_list
