var='ajay'
var1=5
print(var+str(var1)) #we can't add a string with integer.

a='Ajay',' kumar'
print(a)
print(type(a))

b,c='dhoni','csk'
print(b)
print(c)
print(b,c)
d='captain scored againist srilanka'
e=180
f='captain '+b+' scored '+str(e)+' againist srilanka' # If we want add two or more strings we need to concatinate by splitting the string.
print(f)
g='captain %s scored %d againist srilanka'%(b,e) # %s & %d represents string,integer repectively
print(g)
h=f'captain {b} scored {e} againist srilanka'  #In this method also we can get the same output
i='captain {} scored {} againist srilanka'.format(b,e) #In this method also we can get the same output
print(h)
print(i)