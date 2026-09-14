#Q-1
import heapq
# Min Heap
min_heap = []
heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 5)
print("Min Heap:", min_heap)
# Priority Queue
print("Priority Queue:")
while min_heap:
     print(heapq.heappop(min_heap), end=" ")
# Heap Sort
arr = [4, 1, 7, 3, 8, 5]
heap = []
for x in arr:
    heapq.heappush(heap, x)
sorted_arr = []
while heap:
    sorted_arr.append(heapq.heappop(heap))
print("\nHeap Sort:", sorted_arr)



#Q-2
def maximize_difference(arr):
    arr.sort()
    result = []
    left = 0
    right = len(arr) - 1
    while left <= right:
        if left <= right:
            result.append(arr[left])
            left += 1
        if left <= right:
            result.append(arr[right])
            right -= 1
    total = 0
    for i in range(1, len(result)):
        total += abs(result[i] - result[i - 1])
    return result, total
arr = [4, 2, 7, 1]
result, total = maximize_difference(arr)
print("Rearranged Array:", result)
print("Maximum Sum:", total)



#Q-3
def smallest_subarray(arr, target):
    left = 0
    current_sum = 0
    min_length = len(arr) + 1
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum > target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    if min_length == len(arr) + 1:
        return -1

    return min_length


arr = [2, 1, 5, 2, 3, 2]
target = 7

print("Smallest Subarray Length:", smallest_subarray(arr, target))