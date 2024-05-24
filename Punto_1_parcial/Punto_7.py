def f(pos,l):
    return l[pos]+3
p = [4,8,2,9]
g = [4,8,0,2,2,4,3]
a = 2
x = f(2,p) + f(g[a],g)
print (x)
z = f(2,p)
print (z)