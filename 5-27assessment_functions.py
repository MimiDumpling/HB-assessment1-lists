"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

def determines_if_hometown(string="Westminster"):
    """determines, True or False, if a string is the same word as my hometown, Westminster."""

    if string == "Westminster":
        return True

    return False


def writes_full_name(first="Albus", last="Dumbledore"):
    """returns a single string comprised of a first and last name"""

    return "{} {}".format(first, last)
    

def writes_statement_about_hometown(hometown="Westminster", first="Hermione", last="Granger"):
    """prints statement revealing whether or not user is from the same hometown"""

    if determines_if_hometown(hometown) == True:
        print "Hi, {}, we're from the same place!".format(writes_full_name(first, last))
    else:
        print "Hi {}, I'd like to visit {}!".format(writes_full_name(first, last), "Westminster")

print "-- 'PART I' TESTS BEGIN BELOW --"
print
print "-- determines_if_hometown() --"
print
print ('determines_if_hometown("W") == False: ' + str(determines_if_hometown("W") == False))
print ('determines_if_hometown(123) == False: ' + str(determines_if_hometown(123) == False))
print ('determines_if_hometown() == True: ' + str(determines_if_hometown() == True))
print ('determines_if_hometown("Westminster") == True: ' + str(determines_if_hometown("Westminster") == True))
print
print    
print "-- writes_full_name() --"
print
print ('writes_full_name("Mimi", "Nguyen") == Mimi Nguyen: ' + str(writes_full_name("Mimi", "Nguyen") == "Mimi Nguyen"))
print ('writes_full_name(123, "George") == 123 George: ' + str(writes_full_name(123, "George") == "123 George"))
print ('writes_full_name() == Albus Dumbledore: ' + str(writes_full_name() == "Albus Dumbledore"))
print
print
print "-- writes_statement_about_hometown() --"
print
writes_statement_about_hometown("Westminster", "Mimi", "Nguyen")
print "Correct if same: Hi, Mimi Nguyen, we're from the same place!"
print
writes_statement_about_hometown("London", "Mimi", "Bob")
print "Correct if same: Hi Mimi Bob, I'd like to visit Westminster!"
print
writes_statement_about_hometown("London", 123, "Bob")
print "Correct if same: Hi 123 Bob, I'd like to visit Westminster!"
print
writes_statement_about_hometown()
print "Correct if same: Hi, Hermione Granger, we're from the same place!"
print
print " -- THIS ENDS 'PART I' TESTS --"
print
print

###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """
    if fruit == "strawberry" or fruit == "raspberry" or fruit == "blackberry":
        return True
    
    return False



def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    if is_berry(fruit) == True:
        return 0

    return 5


def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """
    return lst + [num]
    


def calculate_price(base_price, state_abrv, tax=.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """

    before_fees = base_price + (base_price * tax)

    if state_abrv == "CA":
        # recyling fee 3%
        total = before_fees + (before_fees * .03)
       
    elif state_abrv == "PA":
        # highway safety fee $2
        total = before_fees + 2

    elif state_abrv == "MA":
        # Commonwealth Fund fee of $1 for items with a base price under $100 
        if base_price < 100:
            total = before_fees + 1

        # Commonwealth Fund fee of $3 for items $100 or more.
        else:
            total = before_fees + 3
    else:
        total = before_fees

    return total


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


def makes_new_list(list, *args):
    # used info from: https://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
    # used info from: https://stackoverflow.com/questions/3394835/args-and-kwargs
    """takes all arguments and combines into single list"""

    for item in args:
        list.append(item)

    return list

print "-- BEGINS TESTS FOR makes_new_list() --"
print 
print ('makes_new_list([1, 2, 3], 4, 5, 6) == [1, 2, 3, 4, 5, 6]: ' + str(makes_new_list([1, 2, 3], 4, 5, 6) == [1, 2, 3, 4, 5, 6]))
print ('makes_new_list(["cat", "dog", "moose"], "bear", "aardvark") == ["cat", "dog", "moose", "bear", "aardvark"]: ' + str(makes_new_list(["cat", "dog", "moose"], "bear", "aardvark") == ["cat", "dog", "moose", "bear", "aardvark"]))
print ('makes_new_list([1, 2, 3], "laptop", " ", 6) == [1, 2, 3, "laptop", " ", 6]: ' + str(makes_new_list([1, 2, 3], "laptop", " ", 6) == [1, 2, 3, "laptop", " ", 6]))

# this test gives a syntax error... will figure out another day
# print ('makes_new_list([1, 2, 3], [4, 5, 6], 7, 8) == [1, 2, 3, [4, 5, 6], 7, 8]: ' + str(makes_new_list([1, 2, 3], [4, 5, 6], 7, 8) == ([1, 2, 3, [4, 5, 6], 7, 8]))
print
print "Different kind of test for same function"
print "Test Output:" + str(makes_new_list([1, 2, 3], [4, 5, 6], 7, 8))
print "Correct if same: [1, 2, 3, [4, 5, 6], 7, 8]"

# this test gives a syntax error... will figure out another day
# print "Output:" + str(makes_new_list([1, [2] 3], [4, 5, 6], 7, 8))
# print "Correct: [1, [2], 3, [4, 5, 6], 7, 8]"
print
print "-- THIS ENDS TESTS FOR makes_new_list() --"
print
print


def creates_tuple_of_word_tripled(word):
    # used info from: https://realpython.com/blog/python/inner-functions-what-are-they-good-for/
    """ prints tuple of original word and tripled original word """
    
    my_tuple = ()

    # inner function
    def multiplies_word_by_three(word):
        return word*3

    # calling inner function
    my_tuple = (word, multiplies_word_by_three(word))

    print my_tuple

print "-- BEGINS TESTS FOR creates_tuple_of_word_tripled() --"
print 
creates_tuple_of_word_tripled("Baby")
print "Correct if same: ('Baby', 'BabyBabyBaby')"
print
creates_tuple_of_word_tripled("Hermione Granger")
print "Correct if same: ('Hermione Granger', 'Hermione GrangerHermione GrangerHermione Granger')"
print
creates_tuple_of_word_tripled("1one1one")
print "Correct if same: ('1one1one', '1one1one1one1one1one1one')"
print
print "-- THIS ENDS TESTS FOR creates_tuple_of_word_tripled() --"
print
print


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
