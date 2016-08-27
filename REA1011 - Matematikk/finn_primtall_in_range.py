
import math
import numpy as np
import time
# findprimes - simple2.py

#range_start = 1
range_start = int(input("\nRange start: \n"))
range_end = int(input("\nRange end: \n"))

                # list comprehension

primes = []              # list which is to have all the found primes

baseclock = time.clock()

#print('Timex : ', 0, ' ms')

all_numbers = np.arange(range_start, range_end, 2, dtype=np.int)

#print('Timey : ', time.clock() - baseclock, ' ms')

a_prime = all_numbers[0]

countertime = 0
while (a_prime < math.sqrt(range_end)):

    #baseclock = time.clock()
    #print('\nTest ' + str(countertime) + '\n:')
    #print('a prime ' + str(a_prime))
    primes.append(a_prime)
    #print('Time append : ', (time.clock() - baseclock)*1000, ' ms')

    #baseclock = time.clock()
    all_numbers = np.delete(all_numbers, 0)
    #print('Time delete : ', (time.clock() - baseclock)*1000, ' ms')
    #print(all_numbers)

    if a_prime == 1:
        primes.append(2)
        pass

    else:
        #baseclock = time.clock()
        delete_these = []
        #print('Time np.zeros : ', (time.clock() - baseclock)*1000, ' ms')

# -----------------------------------

#    Here is were most of the time is spent.

        baseclock = time.clock()

        # TEST 1
        for i in range(0, len(all_numbers)):
            if all_numbers[i] % a_prime == 0:
                delete_these.append(i)


        # TEST 2
        #remain = np.remainder(all_numbers, a_prime)
        #for i in range(0, len(all_numbers)):
        #    if remain[i] == 0:
        #        delete_these.append(all_numbers[i])


        print('Time for loop : %.2f ms' % ((time.clock() - baseclock)*1000))

# ------------------------------------

        #baseclock = time.clock()
        all_numbers = np.delete(all_numbers, delete_these)
        #print('Time delete all num : ', (time.clock() - baseclock)*1000, ' ms')

    a_prime = all_numbers[0]
    countertime += 1


primes.extend(all_numbers)
print("\nNumber of primes: " + str(len(primes)))

print('\nLast prime : ' + str(primes[-1]))


