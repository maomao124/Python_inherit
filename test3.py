"""
 * Project name(项目名称)：Python继承
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 12:57
 * Version(版本): 1.0
 * Description(描述)：
 使用多继承经常需要面临的问题是，多个父类中包含同名的类方法。对于这种情况，Python 的处置措施是：
 根据子类继承多个父类时这些父类的前后次序决定，即排在前面父类中的类方法会覆盖排在后面父类中的同名类方法。
 """


class People:
    def __init__(self):
        self.name = People

    def say(self):
        print("People类", self.name)


class Animal:
    def __init__(self):
        self.name = Animal

    def say(self):
        print("Animal类", self.name)


# People中的 name 属性和 say() 会遮蔽 Animal 类中的
class Person(People, Animal):
    pass


class Person1(Animal, People):
    pass


if __name__ == '__main__':
    zhangsan = Person()
    zhangsan.name = "张三"
    zhangsan.say()
    zhangsan = Person1()
    zhangsan.name = "张三"
    zhangsan.say()
