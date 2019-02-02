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

fib(2000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

