import numpy as np

passrange = np.arange(138241, 674034 + 1)
count = 0

for password in passrange:
    digits = [int(d) for d in str(password)]  # Get each digit

    pass_increase_test = True  # Set defualt pass condition to True
    pass_double_test = False  # Set defualt pass condition to False
    current_digit = None
    for i,d in enumerate(digits):

        if i > 0:
            # If two digits are the same, conditionally pass them
            if digits[i-1] == digits[i]:
                if digits[i] == current_digit:
                    pass_double_test = False
                else:
                    current_digit = digits[i]
                    pass_double_test = True
            if digits[i-1] == digits[i] and digits[i] != current_digit: pass_double_test = True
            if digits[i-1] > digits[i]:
                pass_increase_test = False

    if pass_double_test and pass_increase_test:
        count += 1
print(count)