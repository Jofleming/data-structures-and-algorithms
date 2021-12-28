from linked_list.linked_list import LinkedList, Node

def test_node():
    node = Node("test node")
    actual = node.value
    expected = "test node"
    assert actual == expected

def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

def test_init_linked_list():
    linked_list = LinkedList()
    actual = linked_list.head
    expected = None
    assert actual == expected

def test_add_node_to_empty():
    linked_list = LinkedList()
    linked_list.insert("Test empty")
    actual = linked_list.head.value
    expected = "Test empty"
    assert actual == expected

def test_add_node_to_front():
    linked_list = LinkedList()
    linked_list.insert("test 1")
    linked_list.insert("test 2")
    actual = linked_list.head.value
    expected = "test 2"
    assert actual == expected

def test_includes():
    linked_list = LinkedList()
    linked_list.insert("test includes 1")
    linked_list.insert("test includes 2")
    actual = linked_list.includes("test includes 2")
    expected = True
    assert actual == expected

def test_includes():
    linked_list = LinkedList()
    linked_list.insert("test includes 1")
    linked_list.insert("test includes 2")
    actual = linked_list.includes("test includes 3")
    expected = False
    assert actual == expected

def test_str():
    linked_list = LinkedList()
    linked_list.insert("test string 1")
    linked_list.insert("test string 2")
    linked_list.insert("test string 3")
    actual = str(linked_list)
    expected = "{test string 1} -> {test string 2} -> {test string 3} -> NULL"
