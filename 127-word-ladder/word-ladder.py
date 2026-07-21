class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        while queue:
            word, level = queue.popleft()
            for i in range(len(word)):
                for alphabet in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + alphabet + word[i+1:]

                    if new_word in word_set and new_word not in visited and new_word != word:
                        if new_word == endWord:
                            return level + 1
                        visited.add(new_word)
                        queue.append((new_word, level + 1))
    
        return 0 