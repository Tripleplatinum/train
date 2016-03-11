def funkcja_testowa():
    print "Teraz obadamy te funkcje"
    argument1 = raw_input("podaj liczbe: >")
    print (argument1) + " to twoja liczba"
    argument2 = raw_input("podaj druga liczbe >")
    print (int(argument1) + int(argument2))
    print "Dokonalismy dodawania dwoch argumentow"

    if argument1 > argument2:
        print "Twoja pierwsza liczba jest wieksza od drugiej"
    else:
        print "Twoja druga liczba jest wieksza od pierwszej"

funkcja_testowa()
