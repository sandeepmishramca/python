#variable scope local , global , *args(var args), **kwargs
def scope_test():
    def do_local():
        spam="local spam"
    def do_nonlocal():
        #nonlocal spam
        spam="nonlocal spam"
    def do_global():
        global spam
        spam="global spam"
    spam="test spam"
    do_local()
    print("After local assignment spam ",spam)
    do_nonlocal()
    print("After nonlocal assignment spam ", spam)
    do_global()
    print("After global assignment spam ",spam)

scope_test()
print("In global scope ",spam)


a=0
def my_fuction():
    print a
my_fuction()

def my_function1():
    a=3
    print a
my_function1()
def my_function2():
    global a
    a=3
    print a
my_function2()
print a

a=5
print id(a)
a=8
print id(a)
list1=[1,2,3]
print id(list1)
list1+=[4]
print id(list1)
t=('some','tuple')
print id(t)
t+=('someone','come')
print id(t)
s=str('saneep')
print id(s)
s+="mohan"
print id(s)

def var_fun(*a):
    for i in a:
        print i

def key_word(**kwargs):
    for k,v in kwargs.items():
        print k,v

var_fun(1,2,3,4,5)
my_dict={1:'one',2:'two'}
key_word(value1=1,value2=2)
key_word(**my_dict)