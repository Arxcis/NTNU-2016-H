
import math
# findprimes - simple2.py


set_range_length = int(input("\nWhat range to you want to find primes in?\n"))


all_numbers = [x+1 for x in range(0, set_range_length)]
primes = []


a_prime = all_numbers[0]

while (a_prime < math.sqrt(set_range_length)):
    
    print('a prime ' + str(a_prime))
    primes.append(a_prime)
    del all_numbers[0]
    #print(all_numbers)

    if a_prime == 1:
        pass

    else:
        i=0
        while(1):
            try:
                if all_numbers[i] % a_prime == 0:
                    del all_numbers[i]

                i += 1
            except:
                break

    print("Primes: " + str(len(primes)))
    a_prime = all_numbers[0]


primes.extend(all_numbers)
print("\nNumber of primes: " + str(len(primes)))

print('\nLast prime : ' + str(primes[-1]))

print('\n All primes: \n\n' + str(primes))


