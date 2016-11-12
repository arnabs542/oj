'''
23. Merge k Sorted Lists

Total Accepted: 108193
Total Submissions: 431425
Difficulty: Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

SOLUTION:
    1. Trivial solution: maintain k pointers to k linked lists simultaneously, iterate them to
find the minimum each time to append into the new list. At each time, linearly scan for these
k lists, and we need to do for total n elements, in O(k*n).
    2. Merge these k lists one by one, by merging two of them each time.
2*n/k + 3*n/k + ... + k*n/k = n/k * (k-1)(k+2)/2 = O(kn).
    3. A MIN-HEAP will reduce the time complexity to O(log(k)*n).
    4. DIVIDE AND CONQUER, merge sort two lists at each time. Same asymptotic time complexity,
because we have to merge for logk times, at each time, the time complexity is
O(n): n * logk = nlogk
'''


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # return self.mergeKListsHeap(lists)
        return self.mergeKListsDivideAndConquer(lists)

    def mergeTwoLists(self, l1, l2):
        dummy = node = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return dummy.next

    def mergeKListsDivideAndConquer(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = len(lists) // 2
            left = lists[:mid]
            right = lists[mid:]
            return self.mergeTwoLists(
                self.mergeKListsDivideAndConquer(left),
                self.mergeKListsDivideAndConquer(right))

    def mergeKListsTrivial(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # TODO: Time Limit Exceeded solution, O(k * n)
        k = len(lists)
        nodes = [lists[i] for i in range(k)]
        list_new = node = ListNode(-1)  # use a dummy head
        while True:
            val_min_index = None
            for i in range(k):
                if nodes[i] and (
                        val_min_index is None or
                        nodes[i].val < nodes[val_min_index].val):
                    # print(nodes[i].val)
                    val_min_index = i
            if val_min_index is not None:
                # print('min: ', nodes[val_min_index].val)
                node_new = ListNode(nodes[val_min_index].val)
                nodes[val_min_index] = nodes[val_min_index].next
                node.next = node_new
                node = node_new
            else:
                break

        return list_new.next

    def mergeKListsHeap(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        A min-heap solution
        """
        def compare(x, y):
            if x is None:
                return y is not None
            if y is None:
                return -1
            return x.val - y.val

        heap = Heap(list(lists), compare=compare)
        list_new = node = None
        while heap and heap[0]:
            val_min = heap[0].val
            if not list_new:
                # list_new = node = ListNode(val_min)
                list_new = node = heap[0]
            else:
                # node.next = ListNode(val_min)
                # to avoid instaniation
                node.next = heap[0]
                # XXX: mistake made multiples times, set to its next
                node = node.next
            heap[0] = heap[0].next
            heap.heapify()

        return list_new


class Heap(list):

    def __init__(self, elements, compare=lambda x, y: x - y):
        super(Heap, self).__init__(elements)
        self.compare = compare
        print('size: ', len(self))
        for i in range((len(self) - 2) // 2, -1, -1):
            self.heapify(i)

    def heapify(self, index=0):
        left = 2 * index + 1
        right = 2 * index + 2
        index_min = index
        if left < len(self) and self.compare(
                self[left], self[index_min]) < 0:
            index_min = left
        if right < len(self) and self.compare(
                self[right], self[index_min]) < 0:
            index_min = right
        if index != index_min:
            self[index], self[index_min] = \
                self[index_min], self[index]
            self.heapify(index_min)

    def updateMin(self, value):
        self[0] = value
        self.heapify(0)

def test():
    l = [9, 8, 7, 6, 10, 13, -1]
    heap = Heap(l)
    print(heap)
    assert heap == [-1, 6, 7, 8, 10, 13, 9]
    print('self test passed')
    pass

if __name__ == '__main__':
    test()
