# Random generator

"""
    Idéen her er å bruke sin(tid * skalar) for å generere et random tall. 


"""

import time
import math



max_range = 69999;
min_range = 0;

results = []

normalfordeling = {
    
     '0-9999' : 0,
     '10000-19999' : 0,
     '20000-29999' : 0,
     '30000-39999' : 0,
     '40000-49999' : 0,
     '50000-59999' : 0,
     '60000-69999' : 0
}

for x in range(200000):
    insta_result = math.ceil(max_range * abs(math.sin(time.time()*100.0)))
    results.append(insta_result)

    if 0 <= insta_result <= 9999:
        normalfordeling['0-9999'] += 1

    elif 10000 <= insta_result <= 19999:
        normalfordeling['10000-19999'] += 1

    elif 20000 <= insta_result <= 29999:
        normalfordeling['20000-29999'] += 1

    elif 30000 <= insta_result <= 39999:
        normalfordeling['30000-39999'] += 1

    elif 40000 <= insta_result <= 49999:
        normalfordeling['40000-49999'] += 1

    elif 50000 <= insta_result <= 59999:
        normalfordeling['50000-59999'] += 1

    elif 60000 <= insta_result <= 69999:
        normalfordeling['60000-69999'] += 1



for keys, items in normalfordeling.items():

    print(str(keys) + ' : '+ str(items))

    # The current implementation is not truly random, judging by the normalfordelingskurve.



