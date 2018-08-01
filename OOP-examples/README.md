##OOP学习笔记

1.test08 对于多继承的时候super方法的传参问题, super只能
初始化一个最左边的带有__init__方法的类，其余父类的的初始化，
得单独调用FatherClass.\_\_init__(self, *args)

2.test09 类的多态， 在子类中重写父类的方法

3.test10对象实例化的过程，首先调用\_\_new__方法，\_\_init__方法

4.test11 面向对象-> 类与运算符

5.test12 类的展现 \_\_str__, \_\_repr__, \_\_unicode

6.test13 类的属性控制 \_\_setattr__, \_\_getattr__

7. @property

8. \_\_slots__ 此属性用于限制类添加属性的数量 