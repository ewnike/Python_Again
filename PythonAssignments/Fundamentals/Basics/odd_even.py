
x=2001
def odd_even(x):
    for count in range(x):
        if count % 2 == 0:
            print "The count," + " " + str(count) + ", is even."
        else:
            print "The count," + " " + str(count) + ", is odd."

odd_even(x)
