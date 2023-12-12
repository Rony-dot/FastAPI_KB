"""
normally when we write codes, we load a very big list or very big tuple, or sometimes large dictionary in the memory/ram.
The problem is that, it comes with a cost. Overall the server's memory will get exploited,
and autoscaling groups will create more servers to support more number of requests.
In order to deal with it, we have to judiciously use the resources, for that we need learn generators and iterators.
To understand generators, we need to understand iterators.
Iterator:
    - an iterator is an object, which can be iterated using a loop.
    - it gives us one element at a time.
    - an iterator must implement two methods __iter__() and __next__()
"""

price = [1,2,3,9,8]
price_iter = price.__iter__()

print(price_iter.__next__()) # 1
print(price_iter.__next__()) # 2
print(price_iter.__next__()) # 3

while True:
    try:
        print(price_iter.__next__()) # 9
    except StopIteration:
        break

# custom class for iteration
class InfiniteNaturalNumbers:
    def __init__(self) -> None:
        self.num = 1

    def __iter__(self):
        return self
    def __next__(self):
        num = self.num
        self.num += 1
        return num

values = iter(InfiniteNaturalNumbers())
print(next(values)) # 1
print(next(values)) # 2
print(next(values)) # 3
# printing above inside a loop, will print infinite numbers

"""
generator:
    - smart and intelligent way to create iterators
    - uses iterator internally
"""

def return_values():
    yield 1
    yield 2
    yield "three"

# as we are using generator, that's why the curresponding iterator is already implemented, we need not define anything for it.
value = return_values() # will return an iterator
print(value.__next__()) # 1
print(value.__next__()) # 2
print(value.__next__()) # three
# print(value.__next__()) # StopIteration exception, so use it in try except block
# print(value.__next__()) # StopIteration exception

"""
use case:
    in python range method or loops
real word example:
    if we have a big 100GB csv file, and we want to read it land process each row at once,
    instead of loading the whole csv file in memory,
    we can have an iterator corresponding that file, we can read one row at a time
"""

# Ex 1: generate  the even_numbers < 20
def even_numbers():
    # generate  the even_numbers < 20
    for i in range(0,20):
        if i%2==0:
            yield i

jor_number = iter(even_numbers())
print(jor_number.__next__())
print(jor_number.__next__())
print(jor_number.__next__())
print(jor_number.__next__())
