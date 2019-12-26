import numpy as np

passrange = np.arange(138241, 674034 + 1)
counter = 0

for password in passrange:
    digits = [int(d) for d in str(password)]  # Get each digit

    greaterFlag = True

    doubledDigit = []

    for i in range(1, len(digits)):
        d = digits[i]
        dm1 = digits[i-1]
        # Check for increasing
        if d < dm1:
            greaterFlag = False
            break

    count, unique = np.unique(digits, return_counts=[bool])
    if 2 in count: 
        doubleFlag = True
        print(password)
    else:
        doubleFlag = False

    if doubleFlag and greaterFlag:
        counter += 1
print(counter)
