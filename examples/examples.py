#These examples based on https://www.practicepython.org/ exercise
import random
import json
def exercise1(name,age):
    return name ,' will be 100 year in ',(2017-int(age))+100

def exercise4(num):
    return [x for x in range(1,num) if num%x==0]

def exercise5(l1,l2):
    """comman=[]
    for e in l2:
        if e not in l1:
            comman.append(e)
    return comman"""
    #list comprihension
    return [x for x in l2 if x not in l1]

def exercise8():

    while True:
        ans = raw_input("new or quit")
        num = random.randint(1, 100)
        print num
        if 'quit' == ans:
            break
        else:
            nextnum=int(raw_input("what will be next number "))
            if nextnum==num:
                print 'Congratulation your number is, ',num
            else:
                print ' the Correct num is ', num


def exercise15(l):
    token=l.split()
    #print token[::-1]
    return ' '.join(token[::-1])

def number_compare(numh,guess):
    cowbull=[0,0]
    if numh==guess:
        cowbull[0]+=1
    else:
        cowbull[1]+=1
    return cowbull

#print number_compare(1234,1234)

#l='this is my guide '
#print exercise15(l)

"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print exercise5(a,b)
"""

def get_names():
    input = "D:\data\\names.txt"
    with open(input,'r') as names:
        name_list=names.read().strip().split('\n')
        d={x:name_list.count(x) for x in name_list}
    return d

def get_category_count():
    path="D:\data\images.txt"
    path1 = "D:\\data\\result_images.txt"
    with open(path,'r') as f:
        image_list=f.read().strip().split('/')
        result=[x for x in image_list if len(x)>1 ]
        d={x:result.count(x) for x in result if result.count(x)>1}

    with open(path1,'w') as wfile:
        wfile.write(json.dumps(d))
        #print wfile
    return d

def happy_prime_numbers():
    path ="D:\\data\\happy_number.txt"
    path1="D:\\data\\prime_number.txt"
    with open(path1,'r') as happy:
        happy_list=happy.read().strip().split('\n')
    with open(path1,'r') as prime:
        prime_list=prime.read().strip().split('\n')
    overlaplist =[int(x) for x in prime_list if x in happy_list]
    return overlaplist

def max(*args):
        max=args[0]
        for n in args:
            if max<n:
                max=n
        return max
#print max(34,2,56,9)

def picks_random_word():
    path="D:\data\words.txt"
    with open(path,'r') as f:
        word_list=f.read().strip().split('\n')
        word=random.choice(word_list)
        return word
#print picks_random_word()

def guess_word():
    word='EVAPORATE'
    guessed='_'*len(word)
    word=list(word)
    guessed=list(guessed)
    gussed_list=[]
    letter = raw_input("guess word")
    while True:
        if letter.upper() in gussed_list:
            letter=''
            print "Already guessed"
        elif letter.upper() in word:
            index=word.index(letter.upper())
            guessed[index]=letter.upper()
            word[index]='_'
        else:
            print ''.join(gussed_list)
            if letter.upper() is not '':
                gussed_list.append(letter.upper())
                letter=raw_input("guess word")
        if '_' not in guessed:
            print 'you won!!!'
            break

def add_birthday():
    print "welcome to birthday dictinory!"
    path ="D:\\data\\birthday.json"
    with open(path,'r') as f:
        birthdays=json.load(f)
       # print birthdays['name']
    for name in birthdays:
        print name
    print 'Type "add" to add another birthday. Type "exit" to quit'
    while True:
        print 'who\'s birthday do you want to look up'
        name=raw_input()
        if name=='exit':
            break
        elif name=='add':
            new_name=raw_input('Enter Name')
            new_dob=raw_input('Enter DOB')
            birthdays[new_name]=new_dob
            with open(path,'w') as w:
                json.dump(birthdays,w)
        elif name in birthdays:
            print '{}\'s birthday is {}'.format(name,birthdays[name])
        else:
            print 'sorry we don\'t have {} birthday '.format(name)

#add_birthday()

def read_json():
    path="D:\data\sample.json"
    with open(path,'r') as f:
        jobj=json.load(f)
        print jobj['om_points']
        print jobj['maps'][0]['iscategorical']
        print jobj['maps'][1]['id']
        name='sandeep'
        bir='2018-02-05'
        jobj[name]=bir
        with open(path,'w') as fw:
            json.dump(jobj,fw)
#read_json()
from collections import Counter
def read_dob():
    month=[]
    num_to_string = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    path="D:\\data\\birthday.json"
    with open(path,'r') as j:
        d=json.load(j)
        for name,dob in d.items():
            month.append(num_to_string[int(dob.split('-')[1])])
    print Counter(month)

#read_dob()






