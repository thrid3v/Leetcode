class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = float('inf')
        for i in range(len(arr)-1):
            mindiff = min(mindiff, arr[i+1] - arr[i])
        res = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == mindiff:
                res.append([arr[i], arr[i+1]])
        return res