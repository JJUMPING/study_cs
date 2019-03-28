#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:41:00 2019

@author: jumping
"""


#%%

def is_prime(n):            # 定义 is_prime()，接收一个参数
    if n < 2:              # 开始使用接收到的那个参数（值）开始计算……
        return False       # 不再是返回给人，而是返回给调用它的代码……
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:##循环结束未返回False
        return True   #或者在这里print 调用时continue

for i in range(80, 110):
    if is_prime(i):          # 调用 is_prime() 函数，
        print(i)            # 如果返回值为 True，则向屏幕输出 i
        
#%%

type(3)
type(3.0)
type('3.14')
type(True)
type(range(10))
type([1,2,3])
type((1,2,3))
type({1,2,3})
type({'a':1, 'b':2, 'c':3})

#%%
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

'Awesome' + 'Python'
'Awesome' 'Python'
'Python, ' + 'Awesome! ' * 3
'o' in 'Awesome' and 'o' not in 'Python'
'a' < 'b'
'A' > 'a'
ord('A')
ord('a')
'PYTHON' > 'Python 3'

#%%
for i in range(1, 11, 4):
    print(i)##范围内等差数列

n = 1000
a, b = 0, 1
while a < n:
    print(a, end=' ')#不换行 而改为空格
    a, b = b, a+b
print()
#%%
print('ab\rc')# cb   \r 回到行首c替换a
print('a\n b\rc')   #a换行 b 回到行首替换成c
print('ab \nc')# ab 换行 c

#还原
'''
Simple is better than complex.
Complex is better than complicated.
''' 
#'\nSimple is better than complex.\nComplex is better than complicated.\n'

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
'Now is better than never.'.upper()

# 在 Python 命令行工具之中，单个下划线，是个特殊变量；
# 保存着最近的语句或者表达式的结果
# 上一个 Cell 执行过后，_ 中保存着 'NOW IS BETTER THAN NEVER.' 分次执行
_.lower()
s = 'Now is better than never.'
s.capitalize() # 句首字母大写
s.title() # 每个单词首字母大写
s.swapcase() # 逐个字符更替大小写
s.title().swapcase() 
s = """Simple is better than complex.
Complex is better than complicated."""
#%%
s = """Name,Age,Location
John,18,New York
Mike,22,San Francisco
Janny,25,Miami
Sunny,21,Shanghai"""

r = s.splitlines()[2]   # 取出返回列表中索引值为 2 的那一行
r
r.split()   # 如果没有给 str.split() 传递参数，那么默认为用 None 分割（各种空白，比如，\t 和 \r 都被当作 None）
r.split(sep=',')        
r.split(',')            # 上一行可以这样写。

r.split(sep=',', maxsplit=1)  # 第二个参数指定拆分几次
# r.split(sep=',', 1)         # 上一行不能这样写。
r.split(sep=',', maxsplit=0)  # 0 次，即不拆分
r.split(sep=',', maxsplit=-1) # 默认值是 -1，拆分全部
#%% https://www.cnblogs.com/guigujun/p/6133057.html
# str.isalnum()
print("'1234567890'.isalnum():", \
      '1234567890'.isalnum()) # '3.14'.isalnum() 返回的是 False
#\不影响换行
# str.isalpha()
print("'abcdefghij'.isalpha():", \
      'abcdefghij'.isalpha()) 

# str.isascii()
print("'山巅一寺一壶酒'.isascii():", \
      '山巅一寺一壶酒'.isascii()) 

# str.isdecimal()
print("'0.123456789'.isdecimal():", \
      '0.1234567890'.isdecimal())

# str.isdigit()
print("'0.123456789'.isdigit():", \
      '0.1234567890'.isdigit())       #  注意，如果字符串是 identifier，返回值也是 True

# str.isnumeric()
print("'0.123456789'.isnumeric():", \
      '0.1234567890'.isnumeric())

# str.islower()
print("'Continue'.islower():", \
      'Continue'.islower())

# str.isupper()
print("'Simple Is Better Than Complex'.isupper():", \
      'Simple Is Better Than Complex'.isupper())

# str.istitle()
print("'Simple Is Better Than Complex'.istitle():", \
      'Simple Is Better Than Complex'.istitle())

# str.isprintable()
print("'\t'.isprintable():", \
      '\t'.isprintable())

# str.isspace()
print("'\t'.isspace():", \
      '\t'.isspace())

# str.isidentifier()
print("'for'.isidentifier():", \
      'for'.isidentifier())
s.islower()
s.isdigit()
'1.22'.isdigit()
'1.1'.isdecimal()
#%%容器
import random
alist=[x**2 for x in range(0,5)]
blist=[x**2 for x in range(0,5) if x%2==0]
a_list = [random.randrange(1, 100) for i in range(n)]
clist=[x for x in blist if x!=0]
l1=['q'] 

l2=['w']

l1<l2
#%%
l1=[1]
l1_copy=l1.copy()
l1_sync=l1
l1_copy.append(1)
l1_sync.append('same')
l=l1.append(1)#append操作返回none
print(f'{l1}(1)')
#output：[1, 'same', 1](1)
print('{1} and {0}'.format(l1,l1[1]))
print('{} and {}'.format(l1,l1[1]))#{ord of elem in format}.format(*elem)
#%%
def say_hi(*names):#Arbitrary Positional  Argument 
    for name in names:
        print(f'Hi, {name}!')
say_hi()
say_hi('ann')
say_hi('mike', 'john', 'zeo')
n='mike', 'john', 'zeo'#tuple()
say_hi(n)
say_hi(*n)
n1=['mike', 'john', 'zeo']
say_hi(*n1)#list acts same as tuple, both are treated as containers

a_string = 'Python'
say_hi(*a_string)

a_range = range(10)
say_hi(*a_range)

a_list = list(range(10, 0, -1))
say_hi(*a_list)

a_dictionary = {'ann':2321, 'mike':8712, 'joe': 7610}
say_hi(*a_dictionary)
def say_hi(greeting, *names):#Arbitrary Positional  Argument 可以接收一系列值的位置参数只能有一个；
    #并且若是还有其它位置参数存在，那就必须把这个可以接收一系列值的位置参数排在所有其它位置参数之后。
    for name in names:
        print(f'{greeting}, {name.capitalize()}!')

say_hi('Hello', 'mike', 'john', 'zeo')

def say_hi(greeting, *names, capitalized=False):#  Keyword Argument
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hello', 'mike', 'john', 'zeo')
say_hi('Hello', 'mike', 'john', 'zeo', capitalized=True)
 

def say_hi(**names_greetings):      # Arbitrary Keyword Argument  XX=YY
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')
       
say_hi(mike='Hello', ann='Oh, my darling', john='Hi')

def say_hi(**names_greetings):      #dictionary
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')
        
a_dictionary = {'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'}
say_hi(**a_dictionary)

say_hi(**{'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'})     #**

def say_hi_2(**names_greetings):
    for name in names_greetings:
        print(f'{names_greetings[name]}, {name}!')#single iteration
say_hi_2(mike='Hello', ann='Oh, my darling', john='Hi')
#%%
def is_leap(year):
    leap=False
    if year%4==0:
        if year%100!=0 or year%400==0:
            leap=True
    return leap

def is_leap1(year):
    return year%4==0 and year%100!=0 or year%400==0
year=100
is_leap(year)
is_leap1(year)
#%%
def double_it(n):
    return n * 2

a_list = [1, 2, 3, 4, 5, 6]

b_list = list(map(double_it, a_list))
b_list
b_map=map(double_it, a_list)
c_list = list(map(lambda x: x * 2, a_list))
c_list
#%%
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p: p[1])#按照列表里元组的第二个元素（字符串）排序
pairs
#%%
n=5
def f(n):
    print('\tn =', n)
    if n == 1:
        n=2                             #appear once
        print('Returning...')
        print('\tn =', n, 'return:', 1)
        return 1
    else:
        r = n * f(n-1)
        print('\tn =', n, 'return:', r)
        return r
    
print('Call f(5)...')
print('Get out of f(n), and f(5) =', f(n))
#%%
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = 5              # 这一次，这个变量名称是 n
m = factorial(n)   # n 并不会因此改变；
print(n, m)

def f(n):
    return id(n)
    
n = 5
print(id(n))    # 全局变量 n 的内存地址
print(id(f(n))) # 局部变量 n 的内存地址。
#%%
def is_prime(n):
    """
    Return a boolean value based upon
    whether the argument n is a prime number.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True


help(is_prime)
print(is_prime.__doc__)
is_prime.__doc__
#%%
s = """Gur Mra bs Clguba, ol Gvz Crgref
Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
import this#只要 import this，this.py 中的代码就被执行：????
this.d
this.s
#%%
import datetime

class Golem:
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
    
    def say_hi(self):
        print('Hi!')
        
g = Golem('Clay')
g.name
g.built_year                #self的参数不能用Golem比如Golem.built_year就不行 因为这个attr不属于Golem
g.say_hi
g.say_hi()
type(g)
type(g.name)
type(g.built_year)
type(g.__init__)
type(g.say_hi)
g1 = Golem()#no name
g1.name
g1.built_year
g1.say_hi
g1.say_hi()
class Running_Golem(Golem):      # 刚刚就说，这个圆括号另有用途……
    
    def run(self):
        print("Can't you see? I'm running...")

rg = Running_Golem('Clay')
rg.run
rg.run()
rg.name
rg.built_year
rg.say_hi()
#%%
#import datetime

class Golem:
    __population = 1 #__private variable
    __life_span = 10
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.__population += 1
    
    def say_hi(self):
        print('Hi!')
    
    def cease(self):
        self.__active = False
        Golem.__population -= 1
    
    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease
        return self.__active
    def population(self):
        return Golem.__population    
#    @property#g.population不用（）即可返回其值
#    def population(self):
#        return Golem.__population
g = Golem('Clay')
g.population#返回method描述,可以直接赋值，成为int. #加上@property就不能对其赋值了

# g.population
#Out[140]: <bound method Golem.population of <__main__.Golem object at 0x117f1ff28>>
#
#type(g.population)
#Out[141]: method
#
#Golem.population
#Out[142]: <function __main__.Golem.population(self)>
#
#type(Golem.population)
#Out[143]: function
g.population()#加上@property就变成调用  2()这个不存在的函数
#%%
class Golem:
    __population = 0
    __life_span = 10
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.__population += 1
    
    def say_hi(self):
        print('Hi!')
    
    def cease(self):
        self.__active = False
        Golem.__population -= 1
    
    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease
        return self.__active
    
    @property
    def population(self):
        return Golem.__population
    
    @population.setter
    def population(self, value):
        Golem.__population = value

g = Golem('Clay')
g.population
g.population = 100
ga = Golem('New')
g.population#101
ga.population#101
help(Golem)
Golem.__dict__
g.__dict__
hasattr(Golem, 'population')
getattr(Golem, 'population')
setattr(g, 'population', 10000)
g.population#10000
setattr(g, 'population', 1000)
g.population#1000
ga.population#1000
setattr(Golem, 'population', 10000)
g.population#10000
ga.population#10000  ?????
# 所以，在很多的情况下，不把数据封装在 Class 内部的话，后面会很有很多麻烦。
#%%
class Counter(object):
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            c = self.current
            self.current += 1
        return c

c = Counter(11, 20)
next(c)
next(c)
next(c)
for c in Counter(101, 105):
    print(c, sep=', ')
type(Counter)
#%%
even = (e for e in range(10) if not e % 2)
# odd = (o for o in range(10) if o % 2)
print(even)
for e in even:
    print(e)
sum_of_even = sum(e for e in range(10) if not e % 2)
print(sum_of_even)
#%%
# even = (e for e in range(10) if not e % 2)
odd = [o for o in range(10) if o % 2]
print(odd)
odd
for o in odd:
    print(o)
#%%
    
# even = (e for e in range(10) if not e % 2)
odd = {o for o in range(10) if o % 2}
print(odd)
for o in odd:
    print(o)
#%%

def a_decorator(func):
    def wrapper():
        print('We can do sth. before calling a_func...')
        func()
        print('... and we can do sth. after it was called...')
    return wrapper #not wrapper()?????

@a_decorator
def a_func():
    print("Hi, I'm a_func!")
    
a_func()
#%%
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_restult = original_result.upper()
        return modified_restult
    return wrapper
def strong(func):
    def wrapper():
        original_result = func()
        modified_restult = '<strong>'+original_result+'</strong>'
        return modified_restult
    return wrapper


@uppercase
@strong  #自下而上
def an_output():
    return 'The quick brown fox jumps over the lazy dog.'
print(an_output())

#%%

#%%

#%%

#%%
#%%

#%%

#%%

#%%

#%%

#%%
#%%

#%%

#%%

#%%

#%%

#%%