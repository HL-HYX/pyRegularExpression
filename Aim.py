# #!/usr/bin/env python
# # _*_ coding:utf-8 _*_
# """
# class Ball:
#     def setName(self, name):
#         self.name = name
#     def kick(self):
#         print("我叫%s,该死的，谁踢我"%self.name)

# A = Ball()
# A.setName('胡龙')
# A.kick()
#
#
# # 组合
#
# class Turtle:
#     def __init__(self, x):
#         self.turtle = x
#
#
# class Fish:
#     def __init__(self, y):
#         self.fish = y
#
#
# class Pool:
#     def __init__(self, x, y):
#         self.Turtle = Turtle(x)
#         self.Fish = Fish(y)
#
#
# A = Pool(1, 10)
#
# print("水塘有%d只乌龟,有%d条鱼。" % (A.Turtle.turtle, A.Fish.fish))
#
#
# class C:
#     def __init__(self, size=10):
#         self.size=size
#
#     def get_size(self):
#         return self.size
#
#     def set_size(self, size):
#         self.size=size
#
#     def del_size(self):
#         del self.size
#
#     x=property(get_size(), set_size(), del_size())
#
#
# c1=C()
#
#
# # 运算符的定义
#
# class My_int(int):
#
#     def __add__(self, other):  # 加法行为:+
#         return int.__sub__(self, other)
#
#     def __sub__(self, other):  # 减法行为:-
#         return int.__add__(self, other)
#
#     def __mul__(self, other):  # 乘法行为:*
#         return int.__mul__(self, other)
#
#     def __truediv__(self, other):  # 真除法行为:/
#         return int.__truediv__(self, other)
#
#     def __floordiv__(self, other):  # 整数除法行为:/
#         return int.__floordiv__(self, other)
#
#     def __mod__(self, other):  # 定义取模算法行为:%
#         return int.__mod__(self, other)
#
#     def __divmod__(self, other):  # 定义当被divmod()调用时的行为
#         return int.__divmod__(self, other)
#
#     def __pow__(self, other):  # 定义**运算时的行为
#         return int.__pow__(self, other)
#
#     def __lshift__(self, other):  # 定义按位左移位的行为:<<
#         return int.__lshift__(self, other)
#
#     def __rshift__(self, other):  # 定义按位右移位的行为:>>
#         return int.__rshift__(self, other)
#
#     def __and__(self, other):  # 定义按位与操作的行为:&
#         return int.__and__(self, other)
#
#     def __xor__(self, other):  # 定义按位异或操作的行为:^
#         return int.__xor__(self, other)
#
#     def __or__(self, other):  # 定义按位或操作的行为
#         return int.__or__(self, other)
# """
# import time as g
#
#
# class MyTimer:
#     # 定义类所需的变量
#
#     def __init__(self):
#         self.end = 0
#         self.begin = 0
#         self.calc = 0
#         self.prompt = '未开始计时！！！'
#         self.TIME = ['年', '月', '日', '时', '分', '秒']
#
#     def __str__(self):
#         return self.prompt
#
#     __repr__ = __str__
#
#     # 计时开始
#     def start(self):
#         self.begin = g.localtime()
#         self.prompt = '提示：请调用stop()方法停止计时'
#         print('计时开始。。。')
#
#     # 计时结束
#     def stop(self):
#         if not self.begin:
#             print('提示：请调用start()方法开始计时')
#         else:
#             self.end = g.localtime()
#             self.my_calc()
#             print('计时结束！')
#
#     # 计算时间
#     def my_calc(self):
#         self.calc = []
#         self.prompt = '总共运行了'
#         for index in range(6):
#             self.calc.append(self.end[index] - self.begin[index])
#             if self.calc[index]:
#                 self.prompt += str(self.calc[index]) + self.TIME[index]
#
#     # 时间加法
#     def __add__(self, other):
#         self.prompt = '总共运行了'
#         self._last = []
#         for index in range(6):
#             self._last.append(self.calc[index] + other.calc[index])
#             if self._last[index]:
#                 self.prompt += str(self._last[index]) + self.TIME[index]
#         return self.prompt
