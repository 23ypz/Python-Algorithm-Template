"""
Floyd为多源最短路算法
用于求图中任意两点间的最短距离
因为求全部的最短路，时间复杂度自然比单源的dijkstra高

定义f[i][j] 为 i 到 j 的最短距离
那么 f[i][j] 可以是从一个中间节点 k 转移过来
即 f[i][j] = min(f[i][j],f[i][k] + f[k][j])


样例
3 3
1 2 1
1 3 5
2 3 2

"""


def main():
    # 有 n 个建筑和 m 条单向道路
    n, m = map(int, input().split())
    inf = float('inf')

    def Floyd():
        f = [[inf] * n for i in range(n)]  # 初始化最大表示一开始都无法到达彼此
        for i in range(n):
            f[i][i] = 0  # 自己到自己的最短路为0
        for i in range(m):
            a, b, c = map(int, input().split())
            f[a - 1][b - 1] = f[b - 1][a - 1] = c

        # 外层枚举中间节点
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j])
        return f

    f = Floyd()
    print(f)


if __name__ == '__main__':
    main()
