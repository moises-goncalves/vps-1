# 使用python的list的嵌套实现二叉树 递归实现[root, left, right]
# 辅助函数
def binary_tree(r):
    return[r,[],[]]  # 返回一个列表，包含根节点、左子树和右子树
# 插入左子树函数
def insert_left(root,new_branch):
    t = root.pop(1)  # 弹出左子树
    if len(t) > 1:  # 如果左子树存在
        root.insert(1,[new_branch,t,[]])  # 将新节点插入到左子树的位置
    else:  # 如果左子树不存在
        root.insert(1,[new_branch,[],[]])  # 直接将节点放进去
    return root  # 返回修改后的树

# 插入右子树函数
def insert_right(root,new_branch):
    t = root.pop(2)  # 弹出右子树
    if len(t) > 1:  # 如果右子树存在
        root.insert(2,[new_branch,[],t])  # 将新节点插入到右子树的位置
    else:  # 如果右子树不存在
        root.insert(2,[new_branch,[],[]])  # 直接将节点放进去
    return root  # 返回修改后的树
# 获取根节点的数据项
def get_root_value(root):
    return root[0]  # 返回根节点的数据项
# 设置根节点的数据项
def set_root_value(root,new_val):
    root[0] = new_val  # 设置根节点的数据项
# 获取左子树
def get_left_child(root):
    return root[1]  # 返回左子树
# 获取右子树
def get_right_child(root):
    return root[2]  # 返回右子树
tree_text = binary_tree(3)  # 创建一个二叉树，根节点为3
insert_left(tree_text,4)  # 插入左子树，节点为4
insert_right(tree_text,5)  # 插入右子树，节点为5
insert_left(get_right_child(tree_text),6)  # 插入右子树的左子树，节点为6
print(tree_text)  # 输出整个树
insert_left(get_left_child(tree_text),7)  # 插入左子树，节点为7
print(tree_text)  # 输出整个树