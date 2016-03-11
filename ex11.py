print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


print "Whats your name?"
name = raw_input()
print "Hi %s! It's very nice to meet you here!" % name
print "Is it cold out there where you're sitting?"
temperature = raw_input()
temperature = str(temperature)
if temperature == 'Yes':
    print "You'd better wear something warm"
else:
    print "Oh it's nice that's hot out there!"
