"""
有一个容量为 V 的背包
商场一共有 N 件物品
第 i 件物品的体积为 Wi，价值为 Vi
求在购买的物品总体积不超过 V 的情况下所能获得的最大价值为多少

定义 dp[i] = x 表示买的物品总体积不超过 i 的情况下所能获得的最大价值 x

如果是0-1背包，即数组中的元素不可重复使用，nums放在外循环，target在内循环，且内循环倒序

样例：
5 20
1 6
2 5
3 8
5 15
3 3

"""


def main():
    N, V = map(int, input().split())
    weight = []
    value = []
    for i in range(N):
        a, b = map(int, input().split())
        weight.append(a)
        value.append(b)

    def function_dp(weight, value):
        dp = [0] * (V + 1)
        for i in range(N):
            w, v = weight[i], value[i]
            for j in range(V, w - 1, -1):
                dp[j] = max(dp[j], dp[j - w] + v)
        return dp[-1]

    def function_dfs(weight, value):
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, c):
            if i < 0:
                return 0 if c <= V else float('-inf')
            if V - c < weight[i]:
                return dfs(i - 1, c)
            else:
                return max(dfs(i - 1, c), dfs(i - 1, c + weight[i]) + value[i])

        return dfs(N - 1, 0)

    print(f"dp求解结果{function_dp(weight, value)}")
    print(f"dfs求解结果{function_dfs(weight, value)}")


if __name__ == '__main__':
    main()
