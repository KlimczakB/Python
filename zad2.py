#Explain the results.
x = 5
x == 5 and 3    #3 - because first part is True(x equal 5) it returns Anything(3)
x == 4 and 3    #False - because first part is False(x not equal 4) it returns False, does not care about Anything(3)
3 and x == 5    #True - because second part is True(x equal 5)
3 and x == 4    #False - because second part is False(x notequal 4)

isinstance(True, int)  #True - bo objekt:True jest typu int
isinstance(True, bool) #True - bo objekt:True jest typu bool
