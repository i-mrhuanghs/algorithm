#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List
# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.lSum = None
        self.rSum = None
        self.mSum = None
        self.iSum = None
    def pushUp(self, l, r):
        self.iSum = l.iSum + r.iSum
        self.lSum = max(l.lSum, l.iSum + r.lSum)
        self.rSum = max(r.rSum, r.iSum, l.rSum)
        self.mSum = max(max(l.mSum, r.mSum), l.rSum + r.lSum)
    
    def get(self, a, l)

        
    def maxSubArray(self, nums: List[int]) -> int:
        return self.__max_sub_array(nums, 0, size - 1)


"""
struct Status {
    int lSum, rSum, mSum, iSum;
};

struct Status pushUp(struct Status l, struct Status r) {
    int iSum = l.iSum + r.iSum;
    int lSum = fmax(l.lSum, l.iSum + r.lSum);
    int rSum = fmax(r.rSum, r.iSum + l.rSum);
    int mSum = fmax(fmax(l.mSum, r.mSum), l.rSum + r.lSum);
    return (struct Status){lSum, rSum, mSum, iSum};
};

struct Status get(int* a, int l, int r) {
    if (l == r) {
        return (struct Status){a[l], a[l], a[l], a[l]};
    }
    int m = (l + r) >> 1;
    struct Status lSub = get(a, l, m);
    struct Status rSub = get(a, m + 1, r);
    return pushUp(lSub, rSub);
}

int maxSubArray(int* nums, int numsSize) {
    return get(nums, 0, numsSize - 1).mSum;
}
"""
# @lc code=end
"""
# 动态规划 O(n) O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0 # 上个位置的子序和
        maxAns = nums[0] # 截止到当前位置上最大的子序和是多少
        for num in nums:
            pre = max(pre + num, num) # 当前位置的子序和 注意当前位置的子序和是上一个位置的子序和与当前数的和 与 当前数之中的最大的值
            maxAns = max(maxAns, pre) # 更新截止到当前位置的最大的子序和
        return maxAns
"""
"""
思路和算法

类似于「线段树求解最长公共上升子序列问题」的 pushUp 操作。

我们定义一个操作 get(a, l, r) 表示查询 aa 序列 [l,r][l,r] 区间内的最大子段和，那么最终我们要求的答案就是 get(nums, 0, nums.size() - 1)。如何分治实现这个操作呢？对于一个区间 [l,r][l,r]，我们取 m = \lfloor \frac{l + r}{2} \rfloorm=⌊ 
2
l+r
​
 ⌋，对区间 [l,m][l,m] 和 [m+1,r][m+1,r] 分治求解。当递归逐层深入直到区间长度缩小为 11 的时候，递归「开始回升」。这个时候我们考虑如何通过 [l,m][l,m] 区间的信息和 [m+1,r][m+1,r] 区间的信息合并成区间 [l,r][l,r] 的信息。最关键的两个问题是：

我们要维护区间的哪些信息呢？
我们如何合并这些信息呢？
对于一个区间 [l,r][l,r]，我们可以维护四个量：

\textit{lSum}lSum 表示 [l,r][l,r] 内以 ll 为左端点的最大子段和
\textit{rSum}rSum 表示 [l,r][l,r] 内以 rr 为右端点的最大子段和
\textit{mSum}mSum 表示 [l,r][l,r] 内的最大子段和
\textit{iSum}iSum 表示 [l,r][l,r] 的区间和
以下简称 [l,m][l,m] 为 [l,r][l,r] 的「左子区间」，[m+1,r][m+1,r] 为 [l,r][l,r] 的「右子区间」。我们考虑如何维护这些量呢（如何通过左右子区间的信息合并得到 [l,r][l,r] 的信息）？对于长度为 11 的区间 [i, i][i,i]，四个量的值都和 \textit{nums}[i]nums[i] 相等。对于长度大于 11 的区间：

首先最好维护的是 \textit{iSum}iSum，区间 [l,r][l,r] 的 \textit{iSum}iSum 就等于「左子区间」的 \textit{iSum}iSum 加上「右子区间」的 \textit{iSum}iSum。
对于 [l,r][l,r] 的 \textit{lSum}lSum，存在两种可能，它要么等于「左子区间」的 \textit{lSum}lSum，要么等于「左子区间」的 \textit{iSum}iSum 加上「右子区间」的 \textit{lSum}lSum，二者取大。
对于 [l,r][l,r] 的 \textit{rSum}rSum，同理，它要么等于「右子区间」的 \textit{rSum}rSum，要么等于「右子区间」的 \textit{iSum}iSum 加上「左子区间」的 \textit{rSum}rSum，二者取大。
当计算好上面的三个量之后，就很好计算 [l,r][l,r] 的 \textit{mSum}mSum 了。我们可以考虑 [l,r][l,r] 的 \textit{mSum}mSum 对应的区间是否跨越 mm——它可能不跨越 mm，也就是说 [l,r][l,r] 的 \textit{mSum}mSum 可能是「左子区间」的 \textit{mSum}mSum 和 「右子区间」的 \textit{mSum}mSum 中的一个；它也可能跨越 mm，可能是「左子区间」的 \textit{rSum}rSum 和 「右子区间」的 \textit{lSum}lSum 求和。三者取大。
这样问题就得到了解决。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""