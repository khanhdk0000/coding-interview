import heapq
def binarySearch(data, val):
    lo, hi = 0, len(data) - 1
    best_ind = lo
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if data[mid] < val:
            lo = mid + 1
        elif data[mid] > val:
            hi = mid - 1
        else:
            best_ind = mid
            break
        # check if data[mid] is closer to val than data[best_ind] 
        if abs(data[mid] - val) <= abs(data[best_ind] - val):
            best_ind = mid
    return best_ind

def insert_into_sorted_array(arr, new_val):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < new_val:
            left = mid + 1
        else:
            right = mid
    arr.insert(left, new_val)

# def cookies(k, A):
#     # Write your code here
#     A.sort()
#     n = len(A)
#     if n == 1 and A[0] < k:
#         return -1
#     if A[0] == 0 and A[1] == 0:
#         return -1
#     idx = n - 1
#     # if A[-1] >= k:
#     #     idx = binarySearch(A, k)
#     # while A[idx] >= k and idx > 0:
#     #     idx -= 1
#     last, secLast = 0, 1
#     res = 0
#     while A[last] < k or A[secLast] < k:
#         newVal = A[last] + 2*A[secLast]
#         insert_into_sorted_array(A, newVal)
#         n += 1
#         last += 2
#         secLast += 2
#         if newVal < k and secLast > n - 1:
#             return -1
#         res += 1
#         if newVal >= k and secLast > n - 1:
#             break
#     return res



def cookies(k, A):
    n = len(A)
    if n == 1 and A[0] < k:
        return -1
    if A[0] == 0 and A[1] == 0:
        return -1
    heap = A[:]
    heapq.heapify(heap)
    res = 0
    while heap[0] < k and len(heap) > 1:
        newVal = heapq.heappop(heap) + 2 * heapq.heappop(heap)
        heapq.heappush(heap, newVal)
        res += 1
    return res if heap[0] >= k else -1
    
input = [1,1,1,1,1]
k = 10
print(cookies(k, input))