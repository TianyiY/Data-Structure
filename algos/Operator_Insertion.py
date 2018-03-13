operator=['', '*']
for i in range(1000, 10000):
    # last digit can not be 0
    if (i%10==0):
        continue
    numList=list(str(i))
    for l in range(len(operator)):
        for m in range(len(operator)):
            for r in range(len(operator)):
                # if operator is not '', the following digit is not '0'
                if (operator[l]!='' and numList[1]=='0') or (operator[m]!='' and numList[2]=='0'):
                    continue
                # combine
                formulaStr=numList[0]+operator[l]+numList[1]+operator[m]+numList[2]+operator[r]+numList[3]
                if (len(formulaStr)>4):
                    if (eval(formulaStr)==int(str(i)[::-1])):    # inverse order
                        print(str(i)+'--->'+formulaStr+'='+str(i)[::-1])

