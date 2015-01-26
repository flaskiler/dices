#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# tkinter_mall.py
# flaskiler
# 2014-12-31

import random

#generera ett slumpmässigt heltal (tärning) mellan 1 och 6
die1 = random.randint(1,6)
print (die1)

if die1 == 1:

#skapa en etta
    print ("   ")
    print (" * ")
    print ("   ")
elif die1 == 2:
#skapa en tvåa
        print ("   ")
        print ("* *")
        print ("   ")
elif die1 == 3:
#skapa en trea
        print ("*  ")
        print (" * ")
        print ("  *")
elif die1 == 4:
#skapa en fyra
        print ("   ")
        print ("* *")
        print ("* *")
elif die1 == 5:
#skapa en femma
        print ("* *")
        print (" * ")
        print ("* *")
elif die1 == 6:
#skapa en sexa
        print ("* *")
        print ("* *")
        print ("* *")

else:
        print ("error")
    
