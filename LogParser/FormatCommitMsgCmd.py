# Generate single commit msgs
def getSingleMsgs():
    msg = ""
    while True:
        try:
            line = raw_input()
        except EOFError:
            break
        msg = msg + line + '\n'
    return msg    

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

# Format one commit msg
def formatMsg(msg):
    def setC(s,n,s2):
        return s[:n] + s2 + s[n+1:]
    msg = msg.strip()
    sp1 = msg.split('\n')
    sp2 = msg.split(':')
    sp3 = msg.split(': ')
    if (len(sp2)>1):
        if (len(sp3)==1):
            msg = setC(msg,msg.find(':'),': ')
        else:
            if (sp2[0] != sp3[0]):
                msg = setC(msg,msg.find(':'),': ')
    if (len(sp1)==2):
        if (len(sp1[0])<=12):
            msg = setC(msg,msg.find('\n'),'')
        else:
            msg = setC(msg,msg.find('\n'),'\n\n')
    if (len(sp1)>2) and (len(msg.split('\n\n'))==1):
        msg = setC(msg,msg.find('\n'),'\n\n')

    return msg

# Format after format.... Sounds a little bit weird ...lol
def fAf(msg):
    msg = msg.strip()
    # replace all ':' to ': '
    n = len(msg)
    for i in range(n-1,-1,-1):
        if ((msg[i]==':')and(msg[i:i+2]!=': ')):
            msg = msg[:i] + ': ' + msg[i+1:]
    # If description is list & subject < 12 letter, then let subject as first desc.
    sp = msg.split('\n')
    sp2 = msg.split('\n\n')
    if (len(sp)>1):
        if (len(sp[0])<12)and(len(sp2) > 1):
            desc = sp2[1]
            ls = desc.split('\n')
            if (ls[0].split('1. ')!=1):
                nonum = ls[0][ls[0].find('1. ')+3:]
            else:
                nonum = ls[0]
            if (len(ls)==1):
                msg = msg[:msg.find('\n\n')]+nonum
            else:
                msg = msg[:msg.find('\n\n')] + nonum + msg[msg.find('\n\n'):]
    # Mark TODO
    sp = msg.split('\n')
    if not checkMsg(msg):
        msg = 'TBD-999: TODO\n\n' + msg
    return msg
    
# Remove all TODO mark
def removeTODO(msg):
    sp = msg.split('\n')
    if (sp[0] == 'TBD-999: TODO'):
        return msg[15:]
    else:
        return msg

# Change Specific Commit Msg
def changeSCommit(msg):
    l = []
    f = open('C:\\CodeEn\\Python27\\PScripts\\LogParser\\list.txt', 'r')
    ls = f.readlines()
    head, tail = 0, 0
    while head<len(ls):
        msgBefore, msgAfter = '', ''
        tail = head
        while ls[tail] != '----------\n':
            tail += 1
        msgBefore = ls[head]
        head = tail + 1
        while ls[tail] != '------------------------------------------------------------\n':
            tail += 1
        for i in range(head,tail):
            msgAfter += ls[i]
        head = tail + 1
        l = l + [(msgBefore.strip(), msgAfter.strip())]
    for (h,m) in l:
        if msg.startswith(h):
            msg = m
    if (len(msg.split(': ')) > 1):
        n = msg.find(': ') + 2
        msg= msg[:n] + msg[n].upper() + msg[n+1:]
    return msg

msg = getSingleMsgs()
msg = removeTODO(msg)
msg = changeSCommit(msg)
# msg = formatMsg(msg)
# msg = fAf(msg)

print msg

