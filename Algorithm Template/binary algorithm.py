'''
什么是二分，有什么用？我们从一个问题引入
给你一个递增数组 a
a = [1,3,4,5,6,7,32,42,53,55,56,69,244,248]
给你一个正整数 x
问：大于等于 x 的数中最小是多少

一个暴力的想法是遍历完数组所有数，当遇到第一个大于等于 x 的数就返回答案
最坏的情况下时间复杂度为 O(n)
我们希望能缩短点时间，就需要用到二分的思想

首先题目说明了数组 a 是递增的
假设数组中间的数 a[mid] > x
那么是不是说明右半边的数都一定大于 x，因为数组元素递增
因此答案只需要从左边找
同理如果 a[mid] < x
那么答案只需要从右边找
当然如果 a[mid] == x
符合要求直接返回就行了

接着从左(右)半边继续这个思路折半判断
可以看出我们将一个数组分割成一半一半又一半
时间复杂度是 O(log2 n) 非常的小
可以优化很多问题

二分也可以用于带询问的题目
时间复杂度 O(nlog2 n)也是可以接受的

有很多种写法 我就推荐一种


注: python也有二分的内置库函数

'''


def main():
    a = [1, 3, 4, 5, 6, 7, 32, 42, 53, 55, 56, 69, 244, 248]
    n = len(a)

    # 有很多种写法 我就推荐一种
    def bisect_l(a,x):
        # 在区间 (left, right) 内询问
        left = -1
        right = len(a)
        while left + 1 < right:
            mid = (left + right) // 2
            if a[mid] >= x:
                right = mid
            else:
                left = mid
        return right

    idx = bisect_l(a,30)
    print(f"二分求出的索引idx为:{idx},值为:{a[idx]}")


    # ---------------------------------------------------------- 二分内置库函数写法 -------------------------------------------------------
    from bisect import bisect_left,bisect_right

    # bisect_left 找到第一个大于等于 x 的索引
    # bisect_right 找到第一个大于 x 的索引

    idx2 = bisect_left(a,30)
    print(f"内置库函数bisect_left求出的索引idx2为:{idx2},值为:{a[idx2]}")

    idx3 = bisect_right(a,7)
    print(f"内置库函数bisect_right求出的索引idx3为:{idx3},值为:{a[idx3]}")


main()
