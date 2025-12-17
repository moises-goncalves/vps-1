"""
优先队列 : 队首出队 队尾根据优先级大小入队
二叉堆 实现优先队列 类似于二叉树的逻辑 使用非嵌套列表
"""
from pythonds.trees.binheap import BinHeap
bh = BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
