class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None

    # Pointers for traversing both linked lists
    ptrA, ptrB = headA, headB

    # Traverse both linked lists until they meet or reach the end
    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA

    # Return the intersection node or None if there is no intersection
    return ptrA

# Example usage:
# Create linked lists A and B with an intersection at node C1
# A: 1 -> 2 \
#            C1 -> C2 -> C3
# B: 9 -> 8 /

# Create nodes
a1 = ListNode(1)
a2 = ListNode(2)
c1 = ListNode("C1")
c2 = ListNode("C2")
c3 = ListNode("C3")
b9 = ListNode(9)
b8 = ListNode(8)

a1.next = a2
a2.next = c1
c1.next = c2
c2.next = c3
b9.next = b8
b8.next = c1  # intersection point

intersection_node = get_intersection_node(a1, b9)

# Print the value of the intersection node (or None if there's no intersection)
print(intersection_node.value if intersection_node else None)

