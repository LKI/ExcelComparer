MAX_DIFFERENT_COUNT = 5

from openpyxl import *

#Mark a difference

wb1 = load_workbook(filename = '1.xlsx', use_iterators = True)
sn1 = wb1.get_sheet_names()
wb2 = load_workbook(filename = '2.xlsx', use_iterators = True)
sn2 = wb2.get_sheet_names()

print "1 has sheet names:", sn1
print "2 has sheet names:", sn2

if (sn1 != sn2):
    print "Two file has different sheets."
else:
    print "Two file has the same sheet name."
print

sn = sn1
for wsn in sn:
    ws1 = wb1.get_sheet_by_name(name = wsn)
    ws2 = wb2.get_sheet_by_name(name = wsn)
    c = ws1.get_highest_column()
    r = ws1.get_highest_row()
    if ((ws2.get_highest_column()!= c) or (ws2.get_highest_row() != r)):
        print "SHEET-",wsn,"-DIFFERDENT: Rows or columns not the same!"
    else:
        flag = True
        diffCount = 0
        for i in range(1,r+1):
            if (diffCount <= MAX_DIFFERENT_COUNT):
                for j in range(1,c+1):
                    if (diffCount <= MAX_DIFFERENT_COUNT):
                        c1 = ws1.cell(None,i,j)
                        c2 = ws2.cell(None,i,j)
                        if (c1):
                            if (c2):
                                if (c1.value != c2.value):
                                    print "SHEET-",wsn,"-DIFFERDENT_VALUE: At (",i,",",j,")",
                                    print "diff FROM",c1.value,"TO",c2.value
                                    diffCount += 1
                                    flag = False
                            else:
                                print "SHEET-",wsn,"-DIFFERDENT_TO_NONE: At (",i,",",j,")",
                                print "diff FROM",c1.value
                                diffCount += 1
                                flag = False
                        else:
                            if (c2):
                                print "SHEET-",wsn,"-DIFFERDENT_TO_NONE: At (",i,",",j,")"
                                print "diff FROM",c2.value
                                diffCount += 1
                                flag = False
                    else:
                        break
            else:
                break
        if flag:
            print "SHEET-",wsn,"-ARE_THE_SAME."
