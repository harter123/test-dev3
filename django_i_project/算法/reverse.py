# 什么是递归：实际上就是自己调用自己的情况，基本上就可以理解为是递归
# 递归的注意点，一定要有一个结束条件，否则就是死循环

"""
递归就是一个函数在它的函数体内调用它自身。执行递归函数将反复调用其自身，每调用一次就进入新的一层。递归函数必须有结束条件。
当函数在一直递推，直到遇到墙后返回，这个墙就是结束条件。
所以递归要有两个要素，结束条件与递推关系
"""

def revers1(num):
    if num < 0:
        return

    print(num)
    revers1(num - 1)
revers1(10)


# 递归比较常见的是遍历树形结构
tmp_dict = {
    "a": 1,
    "b": 2,
    "c": {
        "d": 3,
        "e": 4
    }
}

def visit(tree):
    for key in tree:
        if isinstance(tree[key], dict): #c,
            visit(tree[key]) # 参数 tmp_dict[c], 是一个字典
        else:
            print(tree[key]) # a, b

visit(tmp_dict)