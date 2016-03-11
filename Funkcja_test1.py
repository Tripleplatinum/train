
# -*- coding: utf-8 -*-
def funkcja1(arg1, arg2):
    print "masz %r" % arg1
    print "i msz też" % arg2

    solo = int(raw_input("Podaj ile masz lat"))
    han = int(raw_input("Podaj ile masz wzrostu"))

    print (han * solo), "To jest twoj wzrost"
    
    
funkcja1(100, 200)
