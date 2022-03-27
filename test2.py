"""
 * Project name(项目名称)：Python继承
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 12:54
 * Version(版本): 1.0
 * Description(描述)： 
 """


class People:
    def __init__(self):
        self.name = None

    def say(self):
        print("我是一个人，名字是：", self.name)


class Animal:
    def display(self):
        print("人也是高级动物")


# 同时继承 People 和 Animal 类
# 其同时拥有 name 属性、say() 和 display() 方法
class Person(People, Animal):
    pass


if __name__ == '__main__':
    zhangsan = Person()
    zhangsan.name = "张三"
    zhangsan.say()
    zhangsan.display()
