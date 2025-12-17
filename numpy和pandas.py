""""
numpy 和 pandas 的使用
"""
import numpy as np
# numpy基于矩阵运算
array = np.array([[1,2,3],[4,5,6]]) # 创建一个二维数组
print(array)
print(f"数组是:{array.ndim}维的") # ndim 方法
print(f"行数和列数:{array.shape}") # shape方法输出行数和列数
print(f"元素大小是 : {array.size}") # size方法输出数组元素个数

# 使用numpy创建各种矩阵和数组
a = np.array([1,2,3,4,5],dtype=float) # 也可以定义类型
print(a) # 一维数组
print(a.dtype) # 输出为int64 默认表示为64位 内存大更精确 32位内存小 不精确
print(type(a))
# 定义二维列表
b = np.array([[1,2,3],[2,3,4],[3,4,5]])
print(b)
# 创建一个全是0的矩阵
c = np.zeros((4,4)) # 括号写几行几列
print(c)

# 创建一个全是1的矩阵
d = np.ones((9,9))
print(d)

# 创建一个有序
e = np.array(range(50)).reshape(5,10)
print(e)

# 生成线段
f = np.linspace(1,10,20)
print(f)

# numpy的基础运算
g = np.array([10,20,30,40])
b = np.arange(4)
print(g, b)
c = g - b
print(c)
d = g + b
print(d)
e = g ** 2
print(e)

# 函数运算 sin cos tan
c = 10 * np.sin(a)
print(c > 0) # 返回一个布尔值列表

# 矩阵的运算
matrix1 = np.array([[1,2,3],[2,3,4],[3,4,5]])
matrix2 = np.arange(9).reshape(3,3)
# 这种表示是逐个相乘
false_result = matrix1 * matrix2
# 这种才是矩阵相乘
true_result = np.dot(matrix1,matrix2)
true_result2 = matrix1.dot(matrix2)
print(true_result2)
print(false_result)
print(true_result)


a = np.random.random((4,4)) # 创建一个 4 * 4 矩阵
print(a)
# 写上axis = 1 表示在每一行上操作 axis = 0 表示在每一列上操作
print(np.sum(a,axis = 1)) # 求和
print(np.max(a)) # 最大值
print(np.min(a)) # 最小值

A = np.arange(2,14).reshape(3,4) # 创建一个三行四列数组
# 找数组里面最小元素的下标索引
print(np.argmin(A))
# 最大索引
print(A.argmax())
# 计算平均值
print(A.mean()) # 可以使用axis控制行和列
print(np.average(A)) # 老版本指令只能使用np.average(A) 不能使用A.average()
# 求中位数
print(np.median(A)) # 同 average

# 逐步累加
print(A.cumsum())
print(np.cumsum(A))

# 相邻两个数作差
print(np.diff(A))

# 找出非零得数 输出两个array 第一个表示行数 第二个表示列数 组合起来就是非零元素的位置
print(np.nonzero(A))

# 排序
B = np.arange(14,2,-1).reshape(3,4)
print(B)
print(np.sort(B)) # 对每一行单独从小到大排序

# 矩阵的转置
print(B.T.dot(B)) # B的转置乘以自身
print(B.transpose())
print(np.transpose(B))

# clip(A,a,b) 让数组A里面小于a的变成a 大于b的变成b

AA = np.arange(3,15)
print(AA)
# 一维数组下标索引取值
print(AA[3])

aa = np.arange(3,15).reshape(3,4)
print(aa)
print(aa[1][1]) # 两个索引表示第几行第几列 行从一开始 列从0开始
print(aa[1,1]) # 写法二
print(aa[1,1:2]) # 表示第1行 第一位到第二位的数

# 使用for循环遍历每一行
for row in aa:
    print(row)

# 遍历每一列
for column in aa.T:
    print(column)

# 可以使用flat将一个多维数组转化为一行
print(aa.flatten())
for item in aa.flat:
    print(item,end=",")
print()
# 合并两个array
bb = np.array([1,2,3])[:,np.newaxis]
cc = np.array([2,3,4])[:,np.newaxis] # 添加一个纵向维度维度 [np.newaxis,:] 表示增加一个横向维度
C = np.vstack((bb,cc)) # vertical stack 垂直合并
print(C.shape,cc.shape) # horizontal stack 左右合并
print(C)

print(np.hstack((bb,cc)))
print(np.hstack((bb,cc)).shape)

# transpose做不到将一个横向数组转化为纵向的数组
text_arr = np.array([1,1,1])
print(text_arr.T)

# 使用concatenate方法
ll = np.concatenate((bb,cc,cc,cc,bb),axis=0)
print(ll)
# array 的分割
pp = np.arange(3,15).reshape(3,4)
print(pp)
# 对列进行分割 只能进行等分分割 4列分成三份会报错
print(np.split(pp,2,axis= 1))
# 横向分割 分成3拍
print(np.split(pp,3,axis = 0))

# 下面演示进行不等分分割
print(np.array_split(pp,3,axis = 1))

# 简化分割方法 vsplit hsplit
pp = np.arange(3,15).reshape(3,4)
print(np.vsplit(pp,3))
print(np.hsplit(pp,2))

# numpy-array 赋值
mm = np.arange(4)
a = mm
b = mm
c = a
mm[0] = 11 # 一旦mm的值改变 赋值的变量也会改变
print(mm)
print(a)
b[0:2] = [22,33]
print(mm)
"""

注意 : 在numpy中直接赋值的话表示将两个变量关联起来,
      一个改变另一个也会改变 如果想单纯复制值不想关联的话 
      使用array.copy()方法
"""
d = a.copy()
print(d)
a[0:1] = 22
print(a)
print(d)