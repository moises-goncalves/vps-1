# 定义一个BinaryTree类
class BinaryTree:
    def __init__(self,root_data):
        self.key = root_data # 根的值
        self.left_child = None # 保存指向左子树的引用
        self.right_child = None # 保存指向右子树的引用
    # 插入左子树节点
    def insert_left(self,new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    # 插入右子树节点
    def insert_right(self,new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    # 获取左子树
    def get_left_child(self):
        return self.left_child
    # 获取右子树
    def get_right_child(self):
        return self.right_child

    # 获取根节点的值
    def get_root_val(self):
        return self.key
    # 设置根节点的值
    def set_root_val(self, new_value):
        self.key = new_value
# 测试代码
    def __str__(self):
        left_str = str(self.left_child) if self.left_child else "[]"
        right_str = str(self.right_child) if self.right_child else "[]"
        return f"[{self.key}, {left_str}, {right_str}]"

    # 演示各类方法的有效性
if __name__ == '__main__':
    r = BinaryTree('a')
    print(r)
    r.insert_left('b')
    print(r)
    r.get_left_child().set_root_val('d')
    print(r)
    r.get_left_child().insert_left('e')
    print(r)



