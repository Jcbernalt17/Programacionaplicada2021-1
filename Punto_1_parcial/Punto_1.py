s = "complicated"
g = [[0, 1], [1, 7], [10,11]]
def f (x,y,z):
    return x+y+z
x = f(s[g[0][0]], s[g[1][1]:g[1][1]+3], "r")
print (x)