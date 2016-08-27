
import math
import numpy as np
import time
import pickle
# findprimes - simple2.py


def init_cache():

    primes = [1, 2]

    with open('prime.cache', 'wb') as prime_cache:
        pickle.dump(primes, prime_cache)

    return 0


def print_cache():

    with open('prime.cache', 'rb') as prime_cache:
        primes = pickle.load(prime_cache)

        print(primes)  
    return 0

def trim_liste(liste, start, end):

    return 0


def preload_cache(start, end):

    with open('prime.cache', 'rb') as prime_cache:
        primes = pickle.load(prime_cache)

    last_prime = primes[-1]
        
    if start < last_prime and end <= last_prime:

        complete = True
        trim_liste(primes)
        return complete, primes

    complete = False
    primes = []
    return complete, primes


def dump_cache(primes):

    with open('prime.cache', 'wb') as prime_cache:

        pickle.dump(primes, prime_cache)

    return 0


def prime_crush(range_start, range_end):
    baseclock = time.clock()

    primes = []
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


            print(str(a_prime) + ': Time for loop : %.2f ms' % ((time.clock() - baseclock)*1000))

    # ------------------------------------

            #baseclock = time.clock()
            all_numbers = np.delete(all_numbers, delete_these)
            #print('Time delete all num : ', (time.clock() - baseclock)*1000, ' ms')

        a_prime = all_numbers[0]
        countertime += 1
        primes.extend(all_numbers)

        return primes


def main():
    #range_start = 1
    start = int(input("\nRange start: \n"))
    end = int(input("\nRange end: \n"))


    complete, primes = preload_cache(start, end)

    if complete:
        print('\nPrecomputed!')
        print('\nPrimes:' + str(primes))
        print('\nLast prime : ' + str(primes[-1]))
        print("Number of primes: " + str(len(primes)))

    else:
        print('\nComputing primes...')
        primes = prime_crush(start, end)
        dump_cache(primes)
        print('\nPrimes:' + str(primes))
        print('\nLast prime : ' + str(primes[-1]))
        print("Number of primes: " + str(len(primes)))


if __name__ == "__main__":

    main()
    
    #init_cache()
    #print_cache()


