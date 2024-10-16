'''
什么是前缀和，我们从一个问题引入
给定一个数组 a (1 <= len(a) <= 1e5)
a = [1,5,8,7,4,1,2,6,5,7,8,5]

我们想知道一个区间 [l,r] 的和
我们会遍历 a[l].a[l+1].....a[r]
时间复杂度最坏为 O(n) 即遍历完数组所有数

如果此时我们给定一个询问 q (1 <= q <= 1e5)
每个询问给出 l和r 需要求出区间 [l,r] 之间的和
暴力的做法是每个询问 q 都遍历区间 [l,r]
时间复杂度最坏为 O(n^2) 显然是不行的
我们需要一个 O(1) 的时间复杂度在每个询问中得出答案
就是前缀和的作用了

我们先预处理一个数组 prefix = [0,X0,X1,X2,.....,X(n-1)]
其中 Xi 为索引 0~i 的和
那么区间 [l,r] ( 1 <= l < r <= n )的和就可以表示为
sum(a[l - 1:r]) = prefix[r] - prefix[l - 1]
可以做到 O(1)时间内回答询问


注: python库自带前缀和函数



'''


def main():
    a = [1, 5, 8, 7, 4, 1, 2, 6, 5, 7, 8, 5]
    n = len(a)
    prefix = [0]
    for x in a:
        prefix.append(prefix[-1] + x)

    print(f"前缀和数组{prefix}")
    # 如果我们想知道区间 [3,7] 的数组和(注意不是原数组a的索引)
    l,r = 3,7
    ans1 = prefix[r] - prefix[l - 1]
    print(f"区间[3,7]的数组和为:{ans1}")
    # 暴力求解
    ans2 = 0
    for x in a[l - 1:r]:
        ans2 += x
    print(f"暴力求解区间[3,7]的数组和为{ans2}")



    # --------------------------------------- 以下为python库自带前缀和函数-------------------------------------------------------
    from itertools import accumulate
    pre1 = list(accumulate(a))
    print(f"内置前缀和函数求得前缀和数组{pre1}")

    # 初始化一个首元素
    pre2 = list(accumulate(a,initial=0))
    print(f"内置前缀和函数求得前缀和数组{pre2}")


main()
