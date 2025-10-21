## GERALMENTE, e não em todos os casos, o mergesort 
## é mais utilizado em LinkedList e o quickSort em arrays.
def find_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(l1, l2):
    head = Node()
    tail = head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    ## sempre vai ficar sobrando, portanto, conectamos o resto
    # ou se estiver no caso das listas unitárias, primeira recursividade de construção...
    tail.next = l1 or l2

    return head.next   # head.next pois o next dele ficou lá com o primeiro item da lista

def mergesort(head):
    ##Percepção, toda função recursiva tem uma condição de parada no topo
    ## é um pointeiro unitário, voltamos a recursividade e de forma ordenada.
    if not head or not head.next:
        return head

    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None

    left = mergesort(head)
    right = mergesort(after_middle)

    sorted_list = merge(left,right)

    return sorted_list

class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


node_7 = Node(7)
node_1 = Node(1,node_7)
node_3 = Node(3,node_1)
node_9 = Node(9,node_3)

pointer = mergesort(node_9)
for i in range(4):
    print(pointer.val)
    pointer = pointer.next
    

