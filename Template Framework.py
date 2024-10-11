# ---import start--- #
import sys
import os

sys.setrecursionlimit(100000)  # 设置递归深度，其中100000是你需要设置的新的递归次数。
# from graphlib import TopologicalSorter 拓扑排序的包，但是注意这建边的时候，需要反着来 list(TopologicalSorter(g).static_order())
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
# 使用lru_cache装饰器的时候，一定记得传入参数,@lru_cache(None),表示传入的参数正无穷
from heapq import heapify, heappop, heappush
from math import gcd, sqrt, floor
from bisect import bisect_left, bisect_right

# ---import end ---

# ---Fast IO start---
II = lambda: int(sys.stdin.readline().strip())  # 读取一个用户输入的整数
RS = lambda: sys.stdin.readline().strip()  # 读取用户输入的字符串
MI = lambda: map(int, sys.stdin.readline().strip().split())  # 读取用户输入的多个整数
LII = lambda: list(MI())  # 读取用户输入的一个数组
# ---Fast IO end--- #

# ---常量定义 start--- #
mod1 = int(1e9 + 7)
mod2 = 998244353
inf = float("inf")


# ---常量定义 end---   #

# ------------------------------UserCodeStart-------------------------------#

# ---额外的函数 start--- #

# ---额外的函数 end---   #

def solve():
    return 0


if __name__ == '__main__':
    # t = II()
    t = 1
    for _ in range(t):
        solve()

# -------------------------------UserCodeFinish-------------------------------#
