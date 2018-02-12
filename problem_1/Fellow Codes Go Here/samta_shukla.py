
"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""

# constructor for a Node of singly linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def oddEvenList_Helper(head):
    # base case
    if head.next is None:
        # if list has only one element
        print("in helper")
        return head
    else:
        # if list has 2 or more
        el, ol  = unzip_v1(head)
        newhead = zipboth(el,ol)
        print("in helper")
        print(newhead)
        return newhead


def unzip_v1(head):
    eventracker = head
    oddtracker  = head.next
    listtracker = head.next.next
    oddlist     = oddtracker
    evenlist    = eventracker
    count       = 0
    while listtracker:
        if (count%2 ==0):
            eventracker.next = listtracker
            print("even", count, eventracker.data)
            listtracker = listtracker.next
            eventracker = eventracker.next
            eventracker.next = None
            count +=1
        else:
            oddtracker.next = listtracker
            print("odd", count, oddtracker.data)
            listtracker = listtracker.next
            oddtracker = oddtracker.next
            oddtracker.next = None
            count +=1
    
    tracker = oddlist
    while tracker:
        print("now printing oddlist", tracker.data)
        tracker = tracker.next
    
    tracker = evenlist
    while tracker:
        print("now printing evenlist", tracker.data)
        tracker = tracker.next
    
    return evenlist, oddlist

def zipboth(evenlist,oddlist):
    oddtracker = oddlist
    tracker  = evenlist
    
    # get all even behind odd
    # go to the head of odd
    while tracker.next: # Note the change from tracker to tracker.next
        tracker = tracker.next
    
    # now oddtracker points to null; make it point to 1st element of even list
    while oddtracker:
        tracker.next = oddtracker # change from tracker to tracker.next
        oddtracker   = oddtracker.next
        tracker      = tracker.next
    
    tracker = evenlist
    while tracker:
        print("now printing evenlist", tracker.data)
        tracker = tracker.next
    return evenlist


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
    head =  oddEvenList(head)
    print ("Expected result: 1, 3, 5, 2, 4")
    print ("Your result is {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data, head.next.next.next.data, head.next.next.next.next.data))


if __name__ == "__main__":
    main()
