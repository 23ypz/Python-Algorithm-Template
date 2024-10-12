"""
有一个容量为 V 的背包
商场一共有 N 种物品, 每种物品有无限多个
第 i 件物品的体积为 Wi，价值为 Vi
求在购买的物品总体积不超过 V 的情况下所能获得的最大价值为多少

定义 dp[i] = x 表示买的物品总体积不超过 i 的情况下所能获得的最大价值 x

如果是完全背包，即数组中的元素可重复使用，nums放在外循环，target在内循环。且内循环正序

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

    dp = [0] * (V + 1)

    for _ in range(N):
        w, v = map(int, input().split())
        for j in range(w, V + 1):
            dp[j] = max(dp[j], dp[j - w] + v)

    print(dp[-1])


if __name__ == '__main__':
    main()