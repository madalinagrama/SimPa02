import math
import random        
a = ["Dammit, I'm mad!", 
    "Go hang a salami I'm a lasagna hog."] 
                
c = a[0] 
f = 0
e = len(c)-1 

while not c[f].isalpha():
    f += 1

while not c[e].isalpha():
    e -= 1 

while c[f].lower() == c[e].lower() and f < e:
    f += 1 
    e -= 1 
    if f > e:
        print("No luck this time...")
    while not c[f].isalpha():
        f += 1
    while not c[e].isalpha():
        e -= 1
if f < e:
    print("No luck this time...")
else: 
    print("It's a good day for science..") 

c = a[1] 
f = 0
e = len(c)-1

while not c[f].isalpha():
    f += 1

while not c[e].isalpha():
    e -= 1

while c[f].lower() == c[e].lower() and f < e:
    f += 1
    e -= 1
    if f > e:
            print("No luck this time...")
    while not c[f].isalpha():
        f += 1
    while not c[e].isalpha():
        e -= 1

if f < e:
    print("No luck this time...")
else: 
    print("It's a good day for science..") 
