from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一个区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

"""
自己写的 排序 + 双指针
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        left, right = 0, 1
        
        # 由于数组的长度是不断变化的，所以必须每一次使用 len(intervals) 来重新确认范围
        while right < len(intervals):
            # 如果左侧的区间包含右侧区间，并且左侧区间的右边界大于右侧区域的右边界，更新区间
            if intervals[left][1] >= intervals[right][0]:
                if intervals[left][1] < intervals[right][1]:
                    intervals[left][1] = intervals[right][1]
                intervals.pop(right)
                continue
            left += 1
            right += 1

        return intervals
"""