# 插入排序算法 : Insertion Sort
# 插入排序算法是一种简单直观的排序算法。
# 它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
# 插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），
# 因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
# 插入排序算法的稳定性：稳定
# 插入排序算法的复杂度：O(n^2)
def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index] # 当前值
        position = index # 当前值的位置
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1] # 将前一个值赋给当前位置
            position = position - 1 # 将位置向前移动一位

        alist[position] = current_value # 将当前值赋给当前位置
    return alist
if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print(insertion_sort(alist))