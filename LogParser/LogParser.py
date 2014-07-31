f = open('coor-svn.log', 'r')
lines = f.readlines()
d = {}
for s in lines:
    p = s.split('author')
    if (len(p)==3):
        n = p[1][1:4]
        if (not(n in d)):
            d[n] = True


print d
