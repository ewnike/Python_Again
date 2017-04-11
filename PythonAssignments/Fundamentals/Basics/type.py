
l = ['magical unicorns',19,'hello',98.98,'world']
# l = [1,2,3,4,5.88]
# l = ["Marry had a little lamb."]

if all(isinstance(x, (int, float)) for x in l) is True:
    print "The array you entered is of integer type."
    sum = sum(l)
    print ("Sum:" + str(sum))

elif all(isinstance(x, str) for x in l) is True:
    print "The array you entered is of type string."
    list = list(l)
    print "String:" + str(list)
else:
    strs=""
    Sum= 0
    for x in l:
        if isinstance(x,str):
            strs+= x+ " "

        elif type(x)== int or type(x)== float:
            Sum += x

    print(Sum)
    print (strs)
