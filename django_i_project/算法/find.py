"""
Python 二分查找: 必须要是有序的数组里面查找, 中间值是关键

二分搜索是一种在有序数组中查找某一特定元素的搜索算法。
搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；
如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，
而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。

例子： 有一个0 到 20 的数据，我们需要找到12这个数，
首先我们找到中间值 10， 10 小于 12，应该从右边再找
第二次查找就变成 从 10 到20 查找， 然后找到中间值 15,15 > 12,  应该从左边再找
第三次查找就变成 10 到 15里面查找，然后找到中间值 12 ，结束


比普通的遍历查找效率要高得多  时间复杂度 log 2  n
"""


# 测试数组
arr = [2, 3, 4, 10, 40]
tar = 10


def search(data, target, start, end):
    if start > end:
        return -1

    middle_index = int((start + end ) / 2)
    middle = data[middle_index]
    if middle == tar: # 找到了
        return middle_index

    if middle < target: # 中间值小于 target  # 从右边找
        r = search(data, target, middle_index + 1, end)
    else:  # 中间值小于 target  # 从左边边找
        r = search(data, target, start, middle_index - 1)
    return r

# 函数调用
result = search(arr, tar, 0, len(arr) -1)
print(result)

