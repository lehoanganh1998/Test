import time
import string
import tqdm
#! Set password
real_passwd = "abc"

# #! Compare function
def compare(string1, string2):
    if len(string2) != len(string1):
        return False
    for i in range(len(string2)):
        if string2[i] != string1[i]:
            return False
    return True

#! Compare function
def compare_fix(string1, string2):
    flag = 1
    begin_fix = time.time_ns()
    if len(string2) != len(string1):
        flag = 0
    if flag == 1:
        for i in range(len(string2)):
            if string2[i] != string1[i]:
                flag = 0
    end_fix = time.time_ns()
    duration_fix = end_fix - begin_fix
    
    time.sleep((50000 - duration_fix) / 1000000000)
    if flag == 0:
        return False
    elif flag == 1:
        return True

#! duration
def duration(user_input):
    period = 0
    begin = time.time_ns()
    for i in range(10000):
        compare_fix(real_passwd, user_input)
    end = time.time_ns()
    period += end - begin
    return period


#! timing attack to retrieve the length of the password
periods = []
for i in range(40):
    user_input = "x" * i
    period = duration(user_input)
    periods.append(period)
length = periods.index(max(periods))
print(f"length: {length}")
if length != len(real_passwd):
    print("Wrong length")
    exit()

#! timing attack to retrieve the password
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
temp = ""
print(f"Start retrieving first {length-1} characters")
for i in range(length-1):
    periods_temp = [0] * len(characters)
    for iter in range(50):
        periods = []
        for j in characters:
            user_input = temp + j + "a" * (length - i -1)
            period = duration(user_input)
            periods.append(period)
        periods_temp = [a + b for a, b in zip(periods, periods_temp)]
    letter_found = characters[periods_temp.index(max(periods_temp))]
    print(letter_found)
    temp += letter_found
print("Retrieving the last character using bruteforce")
for letter in characters:
    user_input = temp + letter
    if compare_fix(real_passwd, user_input):
        break
print(f"Last character: {letter}")
print("Password: " + user_input)
