import heapq

def find_k_th_largest(nums, k):
    nums = [-num for num in nums]
    print(nums)
    heapq.heapify(nums)
    print(nums)
    res = float('inf')
    for _ in range(k):
        res = heapq.heappop(nums)

    return -res



listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)
heapq._heappop_max(listForTree)
print(listForTree)
print(heapq.heappop(listForTree))
print(heapq.heappop(listForTree))
print(heapq.heappop(listForTree))
# heapq.heappush(listForTree, -1)
# print(listForTree)

#
# def findKthLargest(nums, k):
#     min_heap = [-float('inf')] * k
#     heapq.heapify(min_heap)
#     print(min_heap)
#     for num in nums:
#         if num > min_heap[0]:
#             print(num)
#             heapq.heappop(min_heap)
#             print(min_heap)
#             heapq.heappush(min_heap, num)
#             print(min_heap)
#     return min_heap[0]
#
#
# findKthLargest([3,2,1,5,6,4], 2)