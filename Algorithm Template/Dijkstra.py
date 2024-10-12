"""
dijkstra算法，一个求单源最短路的算法

运用了贪心的思想，从局部最优到全局最优
需要用到优先队列(堆)的数据结构

dijkstra(e,s)
e 为邻接矩阵
s 为起点


下面代码的样例
3 3
1 2 1
1 3 5
2 3 2

"""


def main():
    from heapq import heappop, heappush
    # 有 n 个建筑和 m 条单向道路
    n, m = map(int, input().split())

    '''
    e[i] 为一个列表 [x1,x2,x3,....xn]
    表示 i 有一条通往 xi 的路
    '''
    e = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        e[a].append((b, c))


    def dijkstra(e, s):
        dis = [float('inf')] * (n + 1)
        dis[s] = 0
        q = [(0, s)]
        vis = set()
        while q:
            _, u = heappop(q)
            if u in vis: continue
            vis.add(u)
            for v, w in e[u]:
                if dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    heappush(q, (dis[v], v))
        return dis

    '''
    dis[i] 表示从建筑 s 到建筑 i 的最短距离
    如果为 inf 为无法从建筑 s 到达建筑 i
    '''
    s = 1
    dis = dijkstra(e, s)
    for i,x in enumerate(dis[1:],1):
        if x == float('inf'):
            print(f"建筑{s}无法到达建筑{i}")
        else:
            print(f"建筑{s}到建筑{i}的最短距离为{x}")


if __name__ == '__main__':
    main()
