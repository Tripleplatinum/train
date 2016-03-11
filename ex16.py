from sys import argv # import from sys argv

script, filename = argv # assign var to argv unpack

print "We're going to erase %r." % filename # printing w filename
print "If you don't want that, hit CTRL-C (^C)." # ctrl + c terminates
print "If you do want that, hit RETURN."

raw_input("?") # getting input from usr

print "Opening the file..."
target = open(filename, "w") # opening filename "w" from write?"

print "Truncating the file. Goodbye!"

target.truncate() # erasing stuff in file

print "Now I'm going to ask you for three lines."

line1= raw_input("Line 1: ") # assigning vars with lines from usr
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

line_combo = (line1 + "\n" + line2 + "\n" + line3 + "\n")
print "I'm going to write these to the file."

target.write(line_combo) 

print "And finally, we close it."
target.close() # closing file == saving
