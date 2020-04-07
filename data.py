import collections
import time
import os
import logging
import multiprocessing
import concurrent.futures
from pprint import pprint
from functools import reduce

# Learning Functional programming in python by Dan Bader
# Immutable and mutable data structures.
# working with collections.
scientist = collections.namedtuple('scientist', ['name', 'field', 'born', 'nobel'])

# Mixing mutable and immutable can be dangerous. We can't alter the data but we can't deleted, that can be an
# issue. For example
data = [
scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
scientist(name='Sally Ridle', field='physics', born=1951, nobel=False),
scientist(name='Vera Rubin', field='astronomy', born=1928,nobel=False),
    ]
# data[0].name = 'Not adam'. This will not work because we're altering an immutable data
del data[0] # This will work because data is a list, which is mutable. Here's how to make fix it

data1 = (
scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
scientist(name='Sally Ridle', field='physics', born=1951, nobel=False),
scientist(name='Vera Rubin', field='astronomy', born=1928,nobel=False),
    )
# del data1[0] Won't work, data1 is a mutable data type (tuples)
# Working with filter.
# filtering collections scientist, and store list of scientist with given nobel into a tuple data3

data3 = tuple(filter(lambda x: x.nobel is True, data))
# --------------------------------------------------------------------------------------------------------------
# working with map function. map: (function, *iretables)

names_and_ages = tuple(
    map(
        lambda x: {
            'name': x.name, 'age': 2020 - x.born
        }, data
    )
)
# --------------------------------------------------------------------------------------------------------------
# working with reduce function. Reduce function needs to be imported from functools
# reduce: (function, sequence[,initial]). Here we going to reduce the output of names_and_ages, just to get the age of
# scientist.
# ({'age': 138, 'name': 'Emmy Noether'},
#  {'age': 153, 'name': 'Marie Curie'},
#  {'age': 90, 'name': 'Tu Youyou'},
#  {'age': 81, 'name': 'Ada Yonath'},
#  {'age': 69, 'name': 'Sally Ridle'},
#  {'age': 92, 'name': 'Vera Rubin'})
# lambda  acc, val: acc + val['age'], names_and_ages , 0
#         0   "Emmy Noether": 0 + 138 so on and forth
# look at collections.defaultdict as an alternative!!

total = reduce(
    lambda acc, val: acc + val['age'], names_and_ages, 0
)
# --------------------------------------------------------------------------------------------------------------
# multilpy processing. allows you to run your functions parallel, spread out over mutiple cpu core. without multy
# processing, running the tranform fuinction took 7.02 seconds. with multy processing tranform ran in 1.04 sec
#import multiprocessing

pprint(data1)
print('\n')
def transform(x):
    print(f'Process{os.getpid()} record {x.name}')
    time.sleep(2)
    result = {'name': x.name, 'age': 2020 - x.born}
    print(f'Done process {os.getpid()} record {x.name}')
    return result
start = time.time()
# pool = multiprocessing.Pool()
# result = pool.map(transform, data1)
# concurrent.futures modules is the newer way of doing asynchronous computation in python. need to import it.
# import concurrent.futures
with concurrent.futures.ProcessPoolExecutor() as executor:
    result = executor.map(transform, data1)
end = time.time()
print(f'\nTime to complete : {end-start:.2f}s\n')

pprint(tuple(result))
