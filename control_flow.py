# x = input('Enter whta you want')
# print(type(x))
# p = int(x)
# print(12.is(any))
# print(type(p))
# print(int(x))
# print(int('1234'))
x = 2
#x = int(input('Enter a number'))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

words = ['cat', 'window', 'defens']
for w in words:
    print(w)

print(words)
for w in words:
    if(len(w) > 6):
        print('Hi Bro')
        words.insert(0, w)
print('Hi this is'+str(words))

for w in words:
    print(w)

for i in range(10):
    print(i)
else:
    print('hi Bro')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
    else:
        print(n, 'is a prime number')


class MyEmpty:
    pass

# while True:
#     pass


print('Hi eeee')


def init(*args):
    pass


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()

fib(2000)
print(fib(10))

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a,b = b, a+b
    return result
print(len(fib2(10)))
s = 'Baital'
print(s.__len__())
#print(pair['alu'])

s = [10, 'hola', {'pillu':'mantri'}, 90]
print(s.__len__())

touple = (1,2,{'hola':'hi'}, 'kulli')
print(type(touple))
print(touple[2])
print(touple[-1])
print(touple[:])
print(touple.__len__())

li = [1,list(touple)]
print(li)

dic = {1:2,3:4}
print(type(dic))

dic = {1,2}
print(type(dic))
print('*****Type Empty******')
dic={1:'paltu'}
print(type(dic))
dic = []
print(type(dic))
dic = ()
print(type(dic))


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries -1
        if retries < 0 :
            raise ValueError()

# ask_ok('Do you really want to quit?')


i = 5

def f(val=i):
    print(val)
i='vante matram'
f()

print('*****Another Session******')
print('*****Another Session******')

def f_list(a, L=[]):
    L.append(a)
    return L

print(f_list(1))
print(f_list(2))
print(f_list(3))
s = None
print(type(s))
print(s)






