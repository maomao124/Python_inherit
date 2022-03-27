"""
 * Project name(项目名称)：Python继承
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 12:52
 * Version(版本): 1.0
 * Description(描述)： 实现继承的类称为子类，被继承的类称为父类
 class 类名(父类1, 父类2, ...)：
    #类定义部分
如果该类没有显式指定继承自哪个类，则默认继承 object 类（object 类是 Python 中所有类的父类，
即要么是直接父类，要么是间接父类）。另外，Python 的继承是多继承机制（和 C++ 一样），即一个子类可以同时拥有多个直接父类。

 """


class Shape:
    def draw(self, content):
        print("画", content)


class Form(Shape):
    def area(self):
        print("此图形的面积为...")


if __name__ == '__main__':
    f = Form()
    f.draw("饼")
    f.area()
