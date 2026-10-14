class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        passengers = 0
        minHeap = [] # [end, passNum]

        trips.sort(key = lambda x:x[1])

        for trip in trips:
            passNum, start, end = trip
            while minHeap and minHeap[0][0] <= start:
                passengers -= minHeap[0][1]
                heapq.heappop(minHeap)

            passengers += passNum
            if passengers > capacity:
                return False
            heapq.heappush(minHeap, [end, passNum])
        
        return True


        