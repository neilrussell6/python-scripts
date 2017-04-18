from sys import argv
from random import randint
import time

# ---------------------------------------------
# usage
# python ordered-search.py [data size]
# ---------------------------------------------

script, data_size = argv

search = randint(0, int(data_size))
in_data = range(1, int(data_size) + 1)

# ---------------------------------------------

print "algorithm\t\t| data size\t| search\t| iterations\t| seconds"
print "-" * 80

if (len(data_size) < 6) : output_formatter = "%s\t| %s\t\t| %d\t\t| %d\t\t| %.5f"
else : output_formatter = "%s\t| %s\t| %d\t| %d\t| %.5f"

# ---------------------------------------------
# linear search (loop)
# ---------------------------------------------

start_time = time.time()

def linearSearchLoop( data, search_value ):
    "do a linear search for given value and return the iteration point at which it suceeded"

    for i, n in enumerate(data):
        if (int(n) == search_value) : return i + 1

    return -1

result = linearSearchLoop(in_data, search)
elapsed_time = time.time() - start_time

print output_formatter % ('linear (for loop)', data_size, search, result, elapsed_time)

# ---------------------------------------------
# binary search (loop)
# ---------------------------------------------

start_time = time.time()

def binarySearchLoop( data, search_value ):
    "do a looping binary search for given value and return the iteration point at which it suceeded"

    # set min & max indices
    min_i = 0
    max_i = len(data)
    count = 0

    while (max_i >= min_i):

        count = count + 1
        guess_i = int((min_i + max_i) / 2) # set guess index to avg of remaining data

        # if guess matches search value
        if (data[ guess_i ] == search_value):
            return count # return iteration count

        # if guess was lower than search value
        elif (data[ guess_i ] < search_value):
            min_i = guess_i + 1 # half data for next iteration by increasing the min index

        # if guess was higher than search value
        else:
            max_i = guess_i - 1 # half data for next iteration by decreasing the max index

    return -1

result = binarySearchLoop(in_data, search)
elapsed_time = time.time() - start_time

print output_formatter % ('binary (while loop)', data_size, search, result, elapsed_time)

# ---------------------------------------------
# binary search (recursive)
# ---------------------------------------------

start_time = time.time()

def binarySearchRecursive( data, search_value, count = 1 ):
    "do a recursive binary search for given value and return the iteration point at which it suceeded"

    guess_i = int(len(data) / 2) # set guess index to halfway point in data

    # if data reduced to 1 and still not a match
    if (len(data) == 1 and data[ guess_i ] != search_value):
        return -1

    # if guess matches search value
    if (data[ guess_i ] == search_value):
        return count # return iteration count

    # if guess was lower than search value
    elif (data[ guess_i ] < search_value):
        return binarySearchRecursive( data[ guess_i: ], search_value, count + 1 ) # recurse with upper half of remaining data

    # if guess was higher than search value
    else:
        return binarySearchRecursive( data[ :guess_i ], search_value, count + 1 ) # recurse with lower half of remaining data

result = binarySearchRecursive(in_data, search)
elapsed_time = time.time() - start_time

print output_formatter % ('binary (recursive)', data_size, search, result, elapsed_time)
