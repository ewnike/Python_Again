
# value = "It's thanksgiving day. It's my birthday,too!"
# print(value.replace("day"," month"))

# x = [2,54,-2,7,12,98]
# print max(x)
# print min(x)

# x = ["hello",2,54,-2,7,12,98,"world"]
# print [x[0], x[-1]]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

half = len(x)/2
a = x[:half]
b = x[half:]
print "b is: ", b
print "a is: ",  a
b[0] = a
print "b is now: ", b
# print b.insert(0, a)
