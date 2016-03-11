def cheese_and_crackers(cheese_count, boxes_of_crackers): #def function with 2 parameters
    print "You have %d cheeses!" % cheese_count # print string with formatted digit valiue with cheese cnt
    print "You have %d boxes of crackers" % boxes_of_crackers # same
    print "Man, that's enough for a party!" #same just string
    print "Get a blanket.\n" #prints string with escape character \n newline

print "We can just give the function numbers directly:" # prints string
cheese_and_crackers(20, 30) #gives 2 values to the function which returns it in strings


print "OR, we can use variables from out script:" # printing string
amount_of_cheese = 10 # assigining value to variable
amount_of_crackers = 50 #same

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #giving variable to function, with values assigned before

print "We can even do math inside too:" # printing string
cheese_and_crackers(10 + 20, 5 + 6) # giving math values straight to the function parameters

print "And we can combine the two, variables and math:" # printing string
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # mixing the var given to function parameter with math operators and values

