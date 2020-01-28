import numpy as np
import itertools
from tqdm import tqdm

i = 0

intcode_master = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]

avars = np.arange(5)

maxVar = 0
maxArr = []
for opts in list(itertools.product(avars,avars,avars,avars,avars)):
    outputVar = 0
    for index, inputVar in enumerate(opts):
        # print(opts, index, inputVar)
        runNum = 0
        i = 0
        # print("Running with input: ", inputVar, " and output: ", outputVar)
        intcode = intcode_master
        while True:
            optcodeDigits = [int(d) for d in str(intcode[i])]
            optLen = len(optcodeDigits)
            optcode = int("".join(map(str, optcodeDigits[optLen-2 : optLen])))

            # Set A, B, and C
            if optLen == 1:
                A, B, C = 0,0,0

            elif optLen == 2 and optcode != 99:
                print("Error in optcode ", optcode)
                break
            elif optLen == 3:
                A = 0
                B = 0
                C = optcodeDigits[0]

            elif optLen == 4:
                A = 0
                B = optcodeDigits[0]
                C = optcodeDigits[1]
            
            elif optLen == 5:
                A = optcodeDigits[0]
                B = optcodeDigits[1]
                C = optcodeDigits[2]

            if optcode != 99:
                if C == 0:
                    a1 = intcode[intcode[i+1]]
                else: 
                    a1 = intcode[i+1]

                if optcode not in [3, 4, 99]:
                    if B == 0:
                        a2 = intcode[intcode[i+2]]
                    else:
                        a2 = intcode[i+2]

                # if optcode != [5, 6]:
                #     if A == 0:
                #         a3 = intcode[intcode[i+3]]
                #     else:
                #         a3 = intcode[i+3]

            # print(optcode)
            if optcode == 1:
                intcode[intcode[i+3]] = a1 + a2
                i += 4

            elif optcode == 2:
                intcode[intcode[i+3]] = a1 * a2
                i +=4

            elif optcode == 3:
                a1 = intcode[i+1]
                # inputVar = int(input("Please enter the input:"))
                if runNum == 0:
                    # print("Input ", inputVar)
                    intcode[a1] = inputVar
                    runNum = 1
                elif runNum == 1:
                    # print("Input ", outputVar)
                    intcode[a1] = outputVar
                i+=2

            elif optcode == 4:
                if C == 0:
                    a1 = intcode[i+1]
                    outputVar = intcode[a1]
                elif C == 1:
                    a1 = intcode[i+1]
                    outputVar = a1

                if index == 4 and outputVar > maxVar:
                    maxVar = outputVar
                    maxArr = opts
                    print(maxVar, maxArr)

                i += 2

            # Jump if true
            elif optcode == 5:
                if a1 != 0:
                    i = a2
                else:
                    i += 3

            # Jump if false
            elif optcode == 6:
                if a1 == 0:
                    i = a2
                else:
                    i += 3
            
            # less than
            elif optcode == 7:
                if a1 < a2:
                    intcode[intcode[i+3]] = 1
                else:
                    intcode[intcode[i+3]] = 0
                i += 4

            # equal
            elif optcode == 8:
                if a1 == a2:
                    intcode[intcode[i+3]] = 1
                else:
                    intcode[intcode[i+3]] = 0
                i += 4

            elif optcode == 99:
                # print("Code 99, halting")
                break
print("Max output of ", maxVar, " with options ", maxArr)