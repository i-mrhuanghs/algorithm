#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
import collections
import re
from typing import List
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList) # 转换为set 加快速度
        if not wordList or endWord not in wordList:
            return 0 # 特殊情况判断
        que = collections.deque()
        que.append(beginWord)
        path_dict = dict() # 记录单词对应的长度
        path_dict[beginWord] = 1

        while que:
            word = que.popleft() # 取出队头单词
            word_path = path_dict.get(word) # 获取单词的路径长度
            for i in range(len(word)):
                # 用一个新字母替换word，每次置换一个字母
                chars = list(word)
                for j in range(ord('a'), ord('z')+1):
                    chars[i] = chr(j)
                    new_word = ''.join(chars)
                    # 找到endword，返回当前长度加一
                    if new_word == endWord:# 广搜 先返回的就是最短的
                        return word_path + 1
                    # 如果newword在wordlist中并且没有访问过，则添加访问信息
                    if new_word in wordSet and not path_dict.get(new_word):
                        path_dict[new_word] = word_path+1
                        que.append(new_word)
        return 0


# @lc code=end
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        
        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)
        
        addEdge(beginWord)
        if endWord not in wordId:
            return 0
        
        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)
        
        return 0
"""