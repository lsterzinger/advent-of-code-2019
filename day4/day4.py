import numpy as np

passrange = np.arange(138241, 674034 + 1)
count = 0

for password in passrange:
    digits = [int(d) for d in str(password)]  # Get each digit

    pass_increase_test = True  # Set defualt pass condition to True
    pass_double_test = False  # Set defualt pass condition to False
    for i,d in enumerate(digits):

        if i > 0:
            # If two digits are the same, and they aren't repeated more than twice
            if digits[i-1] == digits[i] and digits[i-2] != digits[i]:
                pass_double_test = True
                current_double = digits[i]

            else: 
                # Otherwise they fail
                pass_double_test = False

            # But they pass again if it's not equal to the old amount
            if digits[i-1] == digits[i] and digits[i-2] != digits[i] and digits[i] != current_double:
                pass_double_test = True
            
            if digits[i-1] > digits[i]:
                pass_increase_test = False

    if pass_double_test and pass_increase_test:
        count += 1
print(count)