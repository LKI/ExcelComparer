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
	
# Check one commit msg
def checkMsg(msg):
    msg = msg.strip()
    def h(s,c,n):
        if (len(s.split(c)) > n):
            return 1
        if (len(s.split(c)) == n):
            return 0
        if (len(s.split(c)) < n):
            return -1
    # Must contain 1orMore '-'
    if (h(msg,'-',1)!=1):
        return False
    # Must contain 1orMore ': '
    if (h(msg,': ',1)!=1):
        return False
    # There must be no more than 2 '\n\n'
    if (h(msg,'\n\n',2)==1):
        return False
    # If has '\n\n' there must be no '\n' before it
    if ((h(msg,'\n\n',1)!=0) and (h(msg.split('\n\n')[0],'\n',1) != 0)):
        return False
    # If has no '\n\n' there must be no '\n'
    if ((h(msg,'\n\n',1)==0) and (h(msg,'\n',1) != 0)):
        return False
    # Better no more than 60 characters
    # if len > 60 then False
    return True
	
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
    if not checkSub(i) or not checkMsg(i):
        n += 1
        of.write(i)
        of.write('----------\n')
        of.write(i)
        of.write('------------------------------------------------------------\n')
print n
of.close()

