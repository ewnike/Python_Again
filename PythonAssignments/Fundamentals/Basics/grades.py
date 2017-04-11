import random

def grades():
    score = (random.randint(50,100))
    print score
    if score > 89:
        print "Your score:" + str(score) + " is an A."
    elif score > 79:
        print "Your score:" + str(score) + " is a B."
    elif score > 69:
        print "Your score:" + str(score) + " is a C."
    elif score > 59:
        print "Your score:" + str(score) + " is a D."
    else:
        print "Please see me about your grade."
grades()
