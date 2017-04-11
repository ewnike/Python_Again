# x=100
# if x <100:
#     print "X is a small number."
# elif x >= 100:
#     print "X is a large number!"
# S = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
# if len(S) < 50:
#     print "Short sentence."
# elif len(S)>= 50:
#     print "Long sentence."
# L = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
# if len(L) < 10:
#     print "Short list."
# elif len(L)>= 10:
#     print "Long list."
x = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
# a = type(x)
# print a
if isinstance(x,str) :
    if len(x) < 50:
        print "Short sentence."
    elif len(x)>= 50:
        print "Long sentence."
elif isinstance(x,int):
    if x <100:
        print "X is a small number."
    elif x >= 100:
        print "X is a large number!"

else:
    if len(x) < 10:
        print "Short list."
    elif len(x)>= 10:
        print "Long list."
