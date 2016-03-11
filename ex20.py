from sys import argv # imports argv function from sys

script, input_file = argv # assigns argv to input_file var

def print_all(f): #defines print_all fnction which prints argument given
    print f.read()

def rewind(f): #defines rewind function and calls method .seek on var f
    f.seek(0)

def print_a_line(line_count, f): #defines print_a_line function with 2 parameters, reads line from second given
    print line_count, f.readline()

current_file = open(input_file) # assigns opend file to current_file (stores it)

print "First let's print the whole file:\n", # prints

print_all(current_file), # sends var current_file as argument to print_all function

print "Now let's rewind, kind of like a tape." # prints

rewind(current_file) # sends current_file var as argumen to rewind function

print "Let's print three lines:" # prints

current_line = 1 # assigns val of var current_line to 1
print_a_line(current_line, current_file) #gives 2 var as args to function print_a_line

current_line += 1 # same but gives +1 to the line which evaluates to the next line (2)
print_a_line(current_line, current_file)

current_line += 1 # 3
print_a_line(current_line, current_file)

