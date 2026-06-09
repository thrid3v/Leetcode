class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for s in range(len(stones)):
            stones[s] = - stones[s]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 < stone2:
                heapq.heappush(stones, stone1-stone2)
        if stones:
            return abs(stones[0])
        return 0

            
        