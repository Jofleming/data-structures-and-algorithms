
# Worked with Taylor White after touching base with a TA.
def merge_linked_lists(list_1, list_2):
    current1 = list_1.head
    current2 = list_2.head
    while current1 and current2:
      temp1 = current1.next
      temp2 = current2.next
      current1.next = current2
      current2.next = temp1
      current1 = temp1
      current2 = temp2
    list_2.head = current2
    return list_1
