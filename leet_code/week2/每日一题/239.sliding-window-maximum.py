#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from typing import List
class MyQueue: #单调队列（从大到小
    def __init__(self) -> None:
        self.queue = []
    #使用list来实现单调队列
    def pop(self,value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)
    #每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    #同时pop之前判断队列当前是否为空。
    #list.pop()时间复杂度为O(n),这里可以使用collections.deque()
    def push(self,value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    #这样就保持了队列里的数值是单调从大到小的了。
    def front(self):
        return self.queue[0]
        
    #查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #先将前k的元素放进队列
        que = MyQueue()
        res = []
        for i in range(k):
            que.push(nums[i])
        res.append(que.front())
        
        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            res.append(que.front())

        #滑动窗口移除最前面元素
        #滑动窗口前加入最后面的元素
        #记录对应的最大值

        return res
# @lc code=end

