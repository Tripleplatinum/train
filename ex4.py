# -*- coding: utf-8 -*-


# definiuje zmienną cars na 100
cars = 100
#deifniuje zmienna na float 4.0
space_in_a_car = 4.0
#definiuje zmienna drivers na 30
drivers = 30
#definiuje zmienna passengers na 90
passengers = 90
# definiuje zmienna cars_not_driven na cars - drivers
cars_not_driven = cars - drivers
# definiuje cars_driven na drajwerów
cars_driven = drivers
# definiuje carpool capacity na wynik działania mnożenia dwóch innych zmiennych
carpool_capacity = cars_driven * space_in_a_car
# defniuje zmienna average_passengers na wynik dzielenia passengers przez cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
