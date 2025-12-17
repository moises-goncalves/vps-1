""""

实际上使用的是后序遍历

"""


import operator
from pythonds import Stack

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

    @staticmethod
    def evaluate(parse_tree):
        opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        left_c = parse_tree.get_left_child()
        right_c = parse_tree.get_right_child()
        if left_c and right_c:
            fn = opers[parse_tree.get_root_val()]
            return fn(BinaryTree.evaluate(left_c), BinaryTree.evaluate(right_c))
        else:
            return parse_tree.get_root_val()

    @staticmethod
    def build_parse_tree(fpexp):
        fplist = fpexp.split()
        pstack = Stack()
        etree = BinaryTree('')
        pstack.push(etree)
        current_tree = etree
        for i in fplist:
            if i == '(':
                current_tree.insert_left('')
                pstack.push(current_tree)
                current_tree = current_tree.get_left_child()
            elif i not in ['+', '-', '*', '/', ')']:
                try:
                    current_tree.set_root_val(int(i))
                except ValueError:
                    current_tree.set_root_val(i)
                parent = pstack.pop()
                current_tree = parent
            elif i == ')':
                current_tree = pstack.pop()
            else:
                current_tree.set_root_val(i)
                current_tree.insert_right('')
                pstack.push(current_tree)
                current_tree = current_tree.get_right_child()

        return etree


if __name__ == '__main__':
    pt = BinaryTree.build_parse_tree("( ( 10 + 5 ) * 3 )")
    print(pt)
    print(BinaryTree.evaluate(pt))




























