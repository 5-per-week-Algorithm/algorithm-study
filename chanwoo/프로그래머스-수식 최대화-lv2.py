from itertools import permutations

from pyparsing import nums

def cal(n1,n2,op):
    if op == '*':
        return n1*n2
    elif op == '+':
        return n1+n2
    else:
       return n1-n2

def solution(expression):

    maxNum = 0
    for priority in permutations([1,2,3],3):
        op = ['*','+','-']
        operatorDict = {
        '*' : priority[0],
        '-' : priority[1],
        '+' : priority[2]
        }
        
        opList = []
        numList = []

        for c in expression:
            if c in op:
                opList.append(c)
        s = expression.replace("*", "+").replace("-","+")
        numList = list(map(int,s.split("+")))
        p = 0
        opStack = []
        numStack =[numList[0]]
        
        for i,o in enumerate(opList):
            if len(opStack) == 0 or operatorDict[o] > operatorDict[opStack[-1]]:
                opStack.append(o) 
                numStack.append(numList[i+1])
                
            else:
                while len(opStack) != 0 and operatorDict[o] <= operatorDict[opStack[-1]]:
                    popedOp = opStack.pop()
                    n2 = numStack.pop()
                    n1 = numStack.pop()
                    numStack.append(cal(n1,n2,popedOp))
                opStack.append(o) 
                numStack.append(numList[i+1])
        
        while opStack:
            popedOp = opStack.pop()
            n2 = numStack.pop()
            n1 = numStack.pop()
            numStack.append(cal(n1,n2,popedOp))
        

        maxNum = max(abs(numStack[0]), maxNum)
    return maxNum
        
s = "177-661X999X99-133+221+334+555-166-144-551-166X166-166X166-133X88X55-11X4+55X888X454X12+11-66+444X99"
s = s.replace("X", "*")
print(solution("1+0-3"))
