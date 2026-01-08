class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashdict = defaultdict(list)

        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord("a")] += 1
            key = tuple(arr)
            hashdict[key].append(word)
        return list(hashdict.values())
