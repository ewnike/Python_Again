l = ['hello','world','my','name','is','Anna']
char = 'o'
strs=""
for word in l:
    if char in word:
        strs += word+ " "
        print strs
