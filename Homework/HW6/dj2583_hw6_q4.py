from DoublyLinkedList import DoublyLinkedList
import copy
def copy_linked_list(lnk_lst):
    main_node = lnk_lst.header.next
    copy_lst = DoublyLinkedList()
    while main_node is not lnk_lst.trailer:
        data_copied = main_node.data
        copy_lst.add_last(data_copied)
        main_node = main_node.next
    return copy_lst

def deep_copy_linked_list(lnk_lst):
    main_node = lnk_lst.header.next
    copy_lst = DoublyLinkedList()

    while main_node is not lnk_lst.trailer:
        deep_data_copied = copy.deepcopy(main_node.data)
        copy_lst.add_last(deep_data_copied)
        main_node = main_node.next

    return copy_lst
