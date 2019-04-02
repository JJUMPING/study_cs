# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=3-2
type(a)
print('jumping',a)
b='23'
bint=int(b)
print(b*3)
#%%
def fc(C):
    f=1.8*C+32
    print(str(f) + 'F')
    return str(f) + 'F'
    
c2f=fc(35)
print(c2f)
#%% calculate the third side of a triangle
#to be fixed
import math
def hypotenuse(a,b):
    hypo=math.sqrt(math.pow(a,2)+math.pow(b,2))
    return 'hypo =' + str(hypo)
c=hypotenuse(3,4)
#%% 
#transfer g to kg
def g2kg(g):
    return str(g/1000) + 'kg'
print(g2kg(2000))
#calculate the third side of a triangle

def Pythagorean_theorem(a,b):
    return 'the third side of a triangle is '+ str((a**2+b**2)**0.5)
print(Pythagorean_theorem(3,4))
PI=3.1415926
a=PI
b=4
str='the third side of a triangle is {}'.format((a**2+b**2)**0.5)
print(str);
print('{1},{1}'.format(4,3))#index

#%% bool operator 
T= 1==1.0
F= 1 is 1.0
True and True
True or False #bool value is true/false
bool(0) #False
bool([]) #False
bool('') #False
bool(False) #False
bool(None) #False
1<2 and 3<4
1<2<3
2>1.5>1#true :not judging from front by step
1<2>1.5#true :not judging from end by step

not False
not None#true
None and 0#None and 0
'M' in 'Magic'
#%%
print(r'\\n\\n')#r'XXX'  no escape char
print('\\\n\\n\\')
print('''
      ...abc
      ...def''')#new line, ... is prompt
str='abc'
print(str)
print('  *',' * *','* * *','   |',sep='\n') #define seperate
#%% 
a=9/3
b=10/3
c=10//3# division
#%%write down a message after filtered 
def text_create(name,msg):
    folder='/Users/jumping/Desktop/learn python/study_cs'
    full_path=folder+name+'.txt'
    file=open(full_path,'w')
    file.write(msg)
    file.close()
    print('done')

def filter(word, censored_word= 'shit', changed_word='gold'):
    return word.replace(censored_word, changed_word)
d=filter('programming is shit')

def text_clean(name, msg):
    clean_msg=filter(msg)
    text_create(name,clean_msg)
msg='programming is shit'
text_clean('clean', msg)
#%% for
for i in range(1,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i, j, j*j))
        if j==9:
            print('\n')

#%% big or small  guess game
def roll_sum(count=3, points=[]):
    import random
    print('>> ROLL THE DICE <<') 
    while count > 0:#'>' not supported between instances of 'list' and 'int'?????
        point=random.randrange(1,7)
        points.append(point)
        count = count-1
    tot=sum(points)
    return tot
g=roll_sum()
#%% big or small  guess game
import random
def roll_dice(count=3, points=None):
     print('<<<<< ROLL THE DICE! >>>>>')
     if points is None:
         points = []
     while count > 0:
         point = random.randrange(1,7)
         points.append(point)
         count = count - 1
     return points
#g=roll_dice()
def result(tot):
    if tot >10:
        return 'Big'
    else:
        return 'Small'

def start_game():
    print('>> START GAME <<')
    yourmoney=1000
    while yourmoney>0:
        yourchoice=input('Big or Small\n')
        choices=['Big','Small']
        if yourchoice in choices:
            bet=int(input('How much you wanna bet\n'))
            points=roll_dice()
            tot=sum(points)
            if result(tot) == yourchoice: # what if "is" instead of "=="  identities are not same
                print('The points are {},You win!'.format(points))
                print('You gain {}, Now you have {}'.format(bet, yourmoney + bet))
                yourmoney=yourmoney + bet
            else:
                print('The points are {},You lose'.format(points))
                print('You lose {}, Now you have {}'.format(bet, yourmoney - bet))
                yourmoney=yourmoney - bet
        else:
            print('invalid guess')
        print('Continue Game')
    else:
        print('game over')
start_game()
   
    
#%%
A=[1,2,3,4]
A.insert(1,2)
A[1:1]=[4]
A[1]='apple'
del A[0]    
#%%
phoneNum='17812345678'
search='345'
print(search + ' is from ' +str(phoneNum.find(search))+' to '+str(phoneNum.find(search)+len(search)))
#%% compound interest
principleAmount=10000
rate=0.1
for i in range(1,10):
    principleAmount=principleAmount*(1+rate)
    print(f'you own {principleAmount} in year {i}')

#%%list
fruit=['apple', 'banana']
fruit.insert(0,'grape')
print(fruit)
fruit.remove('banana')
print(fruit)
fruit[0:0] = ['Orange']
print(fruit)

#fruit=['apple', 'banana']
#fruit[0:1] = 'Oran'# 0:? doesn't matter if ?<len('Oran')
#fruit=['apple', 'banana']
#fruit[0:3] = 'Oran' #cover all and extend

fruit[0:0] = 'Orange'#insert to the first as separate str
print(fruit)
del fruit[0:5]
print(fruit)
fruit[0]='banana'#replace the first 
print(fruit)
fruit[-1]='Orange'
fruit.extend(['pear'])
#%%dic
NASDAQ_code = {'BIDU':'Baidu','SINA':'Sina'}
NASDAQ_code['YOKU'] = 'Youku'
print(NASDAQ_code)
NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
del NASDAQ_code['FB']
NASDAQ_code['TSLA']
#%%tuple
letters = ('a','b','c','d','e','f','g')
letters[0]

#%% set
a_set = {1,2,3,4,'6'}
a_set.add(5)
a_set.discard(5)

#%% data_stracture trick
num_list = [6,2,7,4,1,3,5]
print(sorted(num_list))
sorted(num_list,reverse=True)

for a,b in zip(num_list,str):
    print(b,'is',a)

a = []
for i in range(1,11):
    a.append(i)

b = [i for i in range(1,11)]#列表解析式

import time
a = []
t0 = time.clock()
for i in range(1,20000):
    a.append(i)
print(time.clock() - t0, "seconds process time")
t0 = time.clock()
b = [i for i in range(1,20000)]
print(time.clock() - t0, "seconds process time")

a = [i**2 for i in range(1,10)]
c = [j+1 for j in range(1,10)]
k = [n for n in range(1,10) if n % 2 ==0]
z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
#dic
d = {i:i+1 for i in range(4)}
g = {i:j for i,j in zip(range(1,6),'abcde')}#mapping one by one
g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']#获取元素索引
for num,letter in enumerate(letters):
    print(letter,'is',num + 1)
#%%class
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(coke): # HERE
        print('Energy!')
coke_for_China = CocaCola()
coke_for_China.local_logo = '可口可乐' #
print(coke_for_China.local_logo) #
coke=CocaCola()#'CocaCola' object has no attribute 'local_logo'
#print(coke.local_logo)  cause error
coke = CocaCola()
coke.drink()
coke = CocaCola
coke.drink() == CocaCola.drink(coke)
#%%class2
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    caffeine=140
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(coke): # HERE
        print('Energy!')
coke=CocaCola('可口可乐')
coke.caffeine=0#  change the attr of the instance
print(coke.caffeine)
print(CocaCola.caffeine)#attr of the class unchanged

#%%
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    caffeine=140
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(coke): # HERE
        print('Energy!')
class CaffeineFree(CocaCola):
    caffeine=0

coke_a=CaffeineFree('free')#??free
coke_a.drink()

#%% TEST
class TestA:
    attr = 1
obj_a = TestA()
TestA.attr = 42
print(obj_a.attr)#42

class TestB:
    attr = 1
obj_a = TestB()
obj_b = TestB()
obj_a.attr = 42
print(obj_b.attr)#class unchanged, obj_b unchanged
#%%
from bs4 import beautifulsoup4
soup = BeautifulSoup
print(type(soup))
#%%

#%%

#%%
#%%

