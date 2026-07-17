class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m = len(values)
        n = len(values[0])
        heap = []

        for shop_idx in range(m):
            item_idx = n - 1
            heapq.heappush(heap, (values[shop_idx][item_idx], shop_idx, item_idx))

        total_cost = 0
        day = 1

        while heap:
            val, sh_idx, it_idx = heapq.heappop(heap)
            total_cost += val * day
            day += 1

            if it_idx > 0:
                heapq.heappush(heap, (values[sh_idx][it_idx - 1], sh_idx, it_idx - 1))
        return total_cost
