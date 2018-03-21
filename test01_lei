class Student(object):     #定义一个类，括号内容表示继承自那个类，不知道继承自哪个类就用object类#
    def __init__(self,name,score):#__init__是一个初始化的方法，定义的参数，属性可以在全局中调用，这里的name，score是一个全局参数#
        self.name=name      
        self.score=score
        self.tt=name+'的分数是'+str(score) #全局属性，Python对象可以随意定义增加属性，这里的name，socore是一个变量。#
    def print_score(self,s): 
        print('%s : %s,%s' %(self.name,self.score,self.tt))#全局属性，可以在类中所有法使用#
        print(s)           #s是一个print_socre方法里的私有参数，只能在这个方法中调用，一个方法可以有参数，但是用不用都没有关系，可以没有属性，#
    def print_grade(self):
        if self.score>=90:
            ##return '成绩优秀'  #一个方法（函数）可以不用返回值，返回值不会打印到屏幕上面，返回值是为了赋值方便，没有返回值的方法（函数），调用的时候不用赋值#
            print('成绩优秀')
        elif self.score>=80:
            ##return '成绩良好'
            print('成绩良好')
        elif self.score>=60:
            ##return '成绩及格'
            print('成绩及格')
        else:
            ##return '成绩不及格'
            print('成绩不及格')
b = Student('张三',90)#通过=类名（）创建了一个实例（对象）b,括号里传递的是全局参数的值#
c = Student('李四',80)
d = Student('李四',65)   
b.print_score(6) #实例b调用类中的print_score()方法，以及给类中某方法的一个print_score()私有参数s的值6#
b.print_grade()    
c.print_score(6)
c.print_grade()
d.print_score(6)
d.print_grade()
'''
以下是输出结果
>>> 
张三 : 90,张三的分数是90
6
成绩优秀
李四 : 80,李四的分数是80
6
成绩良好
李四 : 65,李四的分数是65
6
成绩及格
>>> 
'''
'''面向对象最重要的概念就是类（Class）和实例（Instance），
必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，
每个对象都拥有相同的方法，但各自的数据可能不同。
 
小结
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都不相同；
通过在实例变量上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
'''
