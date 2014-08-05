# Generate single commit msgs
def singleMsgs(logFile):
    f = open(logFile, 'r')
    ls = f.readlines()
    l = []
    n = len(ls)
    for i in range(n):
        if (ls[i][0:6]=='commit'):
            msg = ''
            for j in range(i+4, n):
                if (ls[j][0:6]=='commit'):
                    break
                else:
                    if (ls[j]!='\n'):
                        msg = msg + ls[j].strip() + '\n'
            l = l + [msg]
    return l

# Check subject
def checkSub(msg):
    sub = msg.split('\n')[0]
    if (len(sub)<20) or (len(sub)>70):
        return False
    return True

l = singleMsgs('git.log')
of = open('list.txt','w')
n = 0
for i in l:
    if not checkSub(i):
        n += 1
        of.write(i)
        of.write('----------\n')
        of.write(i)
        of.write('------------------------------------------------------------\n')
print n
of.close()

