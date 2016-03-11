
# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10 # przypisuje wartość str zmiennej x oraz podstawia 10 pod %d
binary = "binary" # przypisuje wartość str zmiennej binary
do_not = "don't" # to samo co wyżej zmiennej do_not
y = "Those who know %s and those who %s." % (binary, do_not) # przypsuje str do zmiennej y oraz formatuje str zmiennymi binary i do_not

print x # wyswietla x
print y # wyswietla y

print " I said: %r." % x #wyswietla str oraz format x
print " I also said: '%s'." % y # wyswietla str oraz format y w cudzyslowie

hilarious = False # ustawia zmienna hilarious na False
joke_evaluation = "Isn't that joke so funny?! %r" # ustawia zmienna joke eval na str z formatem %r

print joke_evaluation % hilarious #wyswietla zmienna joke eval zformatowana hilariusem

w = "This is the left side of..." # przypisuje str do zmiennej w
e = "a string with a right side." # przypisuje str do zmiennej e

print w + e # printuje dwiezmienne dodane do siebie
