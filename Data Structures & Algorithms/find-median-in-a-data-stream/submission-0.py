class MedianFinder:

    def __init__(self):
        # use a max heap, to have smaller half of the values
        # min heap, to have the smallest value in the larger half
        self.max_heap_smaller_half = []
        self.min_heap_larger_half = []
        

    def addNum(self, num: int) -> None:
        if not self.max_heap_smaller_half or num <= -self.max_heap_smaller_half[0]:
            heapq.heappush(self.max_heap_smaller_half, -num)
        else:
            heapq.heappush(self.min_heap_larger_half, num)
        
        if len(self.max_heap_smaller_half) < len(self.min_heap_larger_half):
            smallest_larger_value = heapq.heappop(self.min_heap_larger_half)
            heapq.heappush(self.max_heap_smaller_half, -smallest_larger_value)

        elif len(self.max_heap_smaller_half) > len(self.min_heap_larger_half) + 1:
            largest_smaller_value = -heapq.heappop(self.max_heap_smaller_half)
            heapq.heappush(self.min_heap_larger_half, largest_smaller_value)

    def findMedian(self) -> float:
        if len(self.max_heap_smaller_half) == len(self.min_heap_larger_half):
            largest_smaller_value = -self.max_heap_smaller_half[0]
            smallest_larger_value = self.min_heap_larger_half[0]
            return (largest_smaller_value + smallest_larger_value) / 2
        
        return -self.max_heap_smaller_half[0]

        
        