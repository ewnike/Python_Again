def drum_loop(x):
     # go bang on the fourth beat
     if x % 2 == 0:
         print("****")
     else:
         print(" ****")

# prints tish, tish, tish, bang! tish, tish, tish, bang!
for i in range(1,9):
   drum_loop(i)
