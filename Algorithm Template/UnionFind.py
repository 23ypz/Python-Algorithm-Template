"""
并查集，本质上也是一种存图的的方法
适用于找到联通块或分组情况

"""
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1]*n
        self.part = n

    def find(self, x):
        if x != self.root[x]:
            # 在查询的时候合并到顺带直接根节点
            root_x = self.find(self.root[x])
            self.root[x] = root_x
            return root_x
        return x

    def union(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] >= self.size[root_y]:
            # 保证root_x的长度最短
            root_x,root_y = root_y,root_x
        # 将root_x接到root_y上，即x的祖先接到y的祖先，维护最短长度
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]

        self.size[root_x] = 0
        self.part -= 1
        return

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_root_part(self):
        # 获取每个根节点对应的组
        part = defaultdict(list)
        n = len(self.root)
        for i in range(n):
            part[self.find(i)].append(i)
        return part

    def get_root_size(self):
        # 获取每个根节点对应的组大小
        size = defaultdict(int)
        n = len(self.root)
        for i in range(n):
            size[self.find(i)] = self.size[self.find(i)]
        return size


def main():
    # 表示有 5 个节点
    n = 5
    # 表示edges[i][0] 与 edges[i][1] 有一条双向边
    '''
    0 1 2 为一组
    3 4 5 为一组
    '''
    edges = [[0,1],[1,2],[3,5],[3,4]]
    # 初始化并查集,赋值并查集的大小
    uf = UnionFind(n + 1)
    for u,v in edges:
        # 连边
        uf.union(u,v)

    for i in range(n):
        for j in range(i + 1,n):
            if uf.is_connected(i,j):
                print(f"{i}和{j}为一个联通块")
            else:
                print(f"{i}和{j}不是一个联通块")
    print(f"存在{uf.part}个联通块")



if __name__ == '__main__':
    main()