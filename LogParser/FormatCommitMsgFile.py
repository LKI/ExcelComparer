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

    return True

# Format one commit msg
def formatMsg(msg):
    def setC(s,n,s2):
        return s[:n] + s2 + s[n+1:]
    msg = msg.strip()
    sp1 = msg.split('\n')
    sp2 = msg.split(':')
    sp3 = msg.split(': ')
    if (len(sp2)>1) and (len(sp3)==1):
        msg = setC(msg,msg.find(':'),': ')
    if (len(sp1)==2):
        if (len(sp1[0])<=12):
            msg = setC(msg,msg.find('\n'),'')
        else:
            msg = setC(msg,msg.find('\n'),'\n\n')
    if (len(sp1)>2) and (len(msg.split('\n\n'))==1):
        msg = setC(msg,msg.find('\n'),'\n\n')
    if not checkMsg(msg):
        msg = 'TBD-999: TODO\n\n' + msg
        print '-------------------------------------------------'
        print msg
        print '-------------------------------------------------'
    return msg
    

l = singleMsgs('git.log')
for i in l:
    msg = formatMsg(i);

