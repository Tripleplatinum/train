from sys import argv # imports module argv which gives argument from command line

script, filename = argv # assigns variables to unpack argv to,
#first is the name of the scipt, second is the name command line goes to

txt = open(filename) #assign open to var txt, gives filename to open function

print "Here's your file %r:" % filename # prints string + filename
print txt.read() #prints txt function by using .read() command

txt.close()
print "Type the filename again:" #asks user to type filename again
file_again = raw_input(">") #var file_again is waiting for user to input

txt_again = open(file_again) #var txt again is given var file_again in open fnc.

print txt_again.read() # prints file given to txt_again var by .read() command

txt_again.close()
