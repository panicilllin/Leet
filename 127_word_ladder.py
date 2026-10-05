# Leet 127
'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''

# 2026.10.05
# TLE
from collections import deque
class Solution1:
    @staticmethod
    def adjacent(str1, str2) -> bool:
        diff=0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff+=1
        return diff==1

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        if endWord not in wordList:
            return 0
        while queue:
            # print('------')
            # print(f"queue={queue}")
            # print(f"visited={visited}")
            node, length = queue.popleft()
            # print(f"--- node={node}, length={length}")
            if self.adjacent(node, endWord):
                return length+1
            for item in wordList:
                # print(f"item={item} --- node={node}")
                if item in visited:
                    # print(f"skip")
                    continue
                if self.adjacent(node,item):
                    # print(f"add")
                    if item==endWord:
                        return length+2
                    visited.add(item)
                    queue.append((item,length+1))
        return 0

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_list = set(wordList)
        if endWord not in word_list:
            return 0
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            node, step = queue.popleft()
            if node == endWord:
                return step
            alphabets='abcdefghijklmnopqrstuvwxyz'
            for i in range(len(node)):
                for j in alphabets:
                    new_w = node[:i] + j + node[i+1:]
                    # if new_w == node:
                    #     continue
                    # print(f"new_w={new_w}")
                    if new_w in word_list and new_w not in visited:
                        visited.add(new_w)
                        queue.append((new_w, step+1))
                        
        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength("hit", "cog", ["hot","dot","tog","cog"])) # 0
    print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # 5
    