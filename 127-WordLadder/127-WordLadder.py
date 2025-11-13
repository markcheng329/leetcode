# Last updated: 11/13/2025, 4:24:28 AM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        res = 0
        if beginWord == endWord or endWord not in words:
            return 0
        q = deque([beginWord])

        while q:
            res +=1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    for c in range(97,123):
                        if chr(c) == word[j]:
                            continue
                        newword = word[:j] + chr(c) + word[j+1:]
                        if newword in words:
                            words.remove(newword)
                            q.append((newword))
        return 0
