
"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""

#constructor for a Node of singly linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def oddEvenList_Helper(head):
    second = head.next  # The last odd element will point here
    current_odd = head
    current_even = second

    while (current_odd.next is not None) and (current_even.next is not None):
        # Point to the next odd number, then move to it
        current_odd.next = current_odd.next.next
        current_odd = current_odd.next
        
        # Point to the next even number, then move to it
        current_even.next = current_even.next.next
        current_even = current_even.next

    current_odd.next = second
    return head
# =============================================================================
#     #insertion
#     #if len(head)>1:
#     if head == None:
#         return head
#     else:
#         step=0
#         odd = head
#         even = head.next
#         lastodd = head
#         lasteven = head.next
#         while lasteven != None:
#             for i in range(0,step):
#                 lasteven = lasteven.next
#                 
#                 temp = lasteven
#                 
#                 lasteven.next = lasteven
#                 lastodd.next = temp
#                 lastodd = lastodd.next
#             step+=1
#         
#         
#         
#         
#         
#         
# #        odd = head
#         even = head.next
#         lastodd = head
#         lasteven = head.next
#         while lasteven != None:
#             temp = lasteven.next
#             lasteven.next = lasteven
#             lastodd.next = temp
#             lastodd = lastodd.next
#             
#             
# #        lastodd = head
# #        lasteven = head.next
#         
#             
#             
#             even = even.next
#             
#             last = last.next
# #        head = head
# #    else:
#             
#         
#         #loc_idx=0
#         loc_idx=head
#         #mov_idx=0
#         mov_idx=head.next
# #        temp_idx=[]
# #        even_idx=0
#         #keep 1st
#         #while loc_idx<len(head):
#         while mov_idx!= None:
# #        for i in range(0,len(head)):
#         #get the next index, check if it is odd
#             #if head[loc_idx]%2!=0:
#             if loc_idx.data%2!=0:
#                 #mov_idx=loc_idx+1
#                 mov_idx=mov_idx.next
#                 #while head[mov_idx]%2!=1:
#                 while mov_idx.data%2!=1:
#                     #mov_idx=loc_idx+1
#                     mov_idx=mov_idx.next
#             temp = mov_idx
#             while mov_idx.data>loc_idx.data+1:
#                 mov_idx.next=mov_idx
#                 #head[mov_idx]=head[mov_idx-1]
#             head[loc_idx+1] = temp
#         #if odd, pass
#         #if even, keep idx and move to next index
#         #until it meets an odd
#         #Move all even +1 index
#         #insert the odd at the location idx
#         
#     
#         return head
# =============================================================================


#DO NOT CHANGE THIS FUNCTION
def oddEvenList(head):
    return oddEvenList_Helper(head)


#test case
def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head =  oddEvenList(head)
#    print (type(head))
#    print ("{}".format(head.next.data))
    print ("Expected result: 1, 3, 5, 2, 4")
#    print ("Your result is {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data, head.next.next.next.data, head.next.next.next.next.data))
    print ("Your result is {}, {}, {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data, head.next.next.next.data, head.next.next.next.next.data, head.next.next.next.next.next.data, head.next.next.next.next.next.next.data))

if __name__ == "__main__":
    main()