# CITS1401 Project 1 Sem2 2022
# Frederick Leman
# Student Number: 22976862

def main(csvfile, SubjIDs):
    output2 = [OP2(csvfile, SubjIDs[0]), OP2(csvfile, SubjIDs[1])]
    return OP1(csvfile, SubjIDs), output2, OP3(csvfile), OP4(csvfile, SubjIDs)
    
def OP1(csvfile, SubjIDs):
    F1 = SubjIDs[0]
    F2 = SubjIDs[1]
    F1Dict = {}
    F2Dict = {}
    lmkList = ['Ft', 'Ex', 'En', 'Al', 'Sbal', 'Ch']
    capitalsList = ['FT', 'EX', 'EN', 'AL', 'SBAL', 'CH']
    
    for i in range (0, 6):
        with open(csvfile, "r") as infile:
            for line in infile:
                data = line.split(',')
                if (data[0] == F1 or data[0] == F2) and data[1] == lmkList[i]:
                    a = (float(data[5])-float(data[2]))**2
                    b = (float(data[6])-float(data[3]))**2
                    c = (float(data[7].strip())-float(data[4]))**2
                    ans = round((a+b+c)**0.5, 4)
                    if data[0] == F1:
                        F1Dict[capitalsList[i]] = ans
                    else:
                        F2Dict[capitalsList[i]] = ans
                
    OP1List = [F1Dict, F2Dict]
    return OP1List

def OP2(csvfile, F):
    x = []
    FDict = {}
    lmkList = ['Ft', 'Ex', 'En', 'Al', 'Sbal', 'Ch']
    table2 = ['EXEN', 'ENAL', 'ALEX', 'FTSBAL', 'SBALCH', 'CHFT']
    
    for i in range (0, 6):
        with open(csvfile, "r") as infile:
            for line in infile:
                data = line.split(',')
                if data[0] == F and data[1] == lmkList[i]:
                    x.extend([data[2], data[3], data[4]])
    
    EXEN1 = [x[3],x[4],x[5],x[6],x[7],x[8]]
    ENAL = [x[6],x[7],x[8],x[9],x[10],x[11]]
    ALEX = [x[9],x[10],x[11],x[3],x[4],x[5]]
    FTSBAL = [x[0],x[1],x[2],x[12],x[13],x[14]]
    SBALCH = [x[12],x[13],x[14],x[15],x[16],x[17]]
    CHFT = [x[15],x[16],x[17],x[0],x[1],x[2]]
    
    distList = [EXEN1, ENAL, ALEX, FTSBAL, SBALCH, CHFT]
    for i in range (0,6):
        ans = round(euclidian(distList[i]), 4)
        FDict[table2[i]] = ans
        
    return FDict

def euclidian(z):
    y = [float(x) for x in z]
    a = (y[3] - y[0])**2
    b = (y[4] - y[1])**2
    c = (y[5] - y[2])**2
    ans = ((a+b+c)**0.5)
    return ans

def OP3(csvfile):
    tempList = []
    faceAsymList = []
    IDList = []
    OP3 = []
    with open(csvfile, "r") as infile:
        for line in infile:
            data = line.split(',')
            tempList.append(data[0])
        tempList.pop(0)
        IDList = list(set(tempList))
    
    for face in IDList:
        faceList = []
        faceTuple = ()
        with open (csvfile, "r") as infile:
            for line in infile:
                tempList1 = []
                data = line.split(',')
                if data[0] == face:
                    tempList1.extend([data[2], data[3], data[4], data[5], data[6], data[7].strip()])
                    faceList.append(euclidian(tempList1))
            faceTuple = (face, round(float((sum(faceList))), 4))
            faceAsymList.append(faceTuple)
    
    faceAsymList.sort(key = lambda x: x[1])
    OP3 = faceAsymList[:5]
    
    return OP3

def OP4(csvfile, SubjIDs):
    t1 = OP2(csvfile, SubjIDs[0])
    t2 = OP2(csvfile, SubjIDs[1])
    x = [t1['EXEN'], t1['ENAL'], t1['ALEX'], t1['FTSBAL'], t1['SBALCH'], t1['CHFT']]
    y = [t2['EXEN'], t2['ENAL'], t2['ALEX'], t2['FTSBAL'], t2['SBALCH'], t2['CHFT']]
    
    a = (x[0]*y[0]) + (x[1]*y[1]) + (x[2]*y[2]) + (x[3]*y[3]) + (x[4]*y[4]) + (x[5]*y[5])
    i = x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2 + x[5]**2
    j = y[0]**2 + y[1]**2 + y[2]**2 + y[3]**2 + y[4]**2 + y[5]**2
    
    ans = round(a / ((i**0.5) * (j**0.5)), 4)
    return ans

# [OP1, OP2, OP3, OP4] = main('data.csv', ['B7033','C1283'])
