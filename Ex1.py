import time
import string
import tqdm
#! Set password
real_passwd = "lehoanganhabcd"

#! Compare function
def compare(string1, string2):
    if len(string2) != len(string1):
        return False
    for i in range(len(string2)):
        if string2[i] != string1[i]:
            return False
    return True

#! duration
def duration(user_input):
    period = 0
    begin = time.time_ns()
    for i in range(10000):
        compare(real_passwd, user_input)
    end = time.time_ns()
    period += end - begin
    return period


#! timing attack to retrieve the length of the password
periods = []
for i in range(30):
    user_input = "x" * i
    period = duration(user_input)
    periods.append(period)
length = periods.index(max(periods))
print(f"length: {length}")


#! timing attack to retrieve the password
characters = string.ascii_lowercase
temp = ""
print(f"Start retrieving first {length-1} characters")
for i in tqdm.tqdm(range(length-1)):
    periods_temp = [0] * len(characters)
    for iter in range(20):
        periods = []
        for j in characters:
            user_input = temp + j + "a" * (length - i -1)
            period = duration(user_input)
            periods.append(period)
        periods_temp = [a + b for a, b in zip(periods, periods_temp)]
    letter_found = characters[periods_temp.index(max(periods_temp))]
    temp += letter_found
print("Retrieving the last character using bruteforce")
for letter in characters:
    user_input = temp + letter
    if compare(real_passwd, user_input):
        break
print(f"Last character: {letter}")
print("Password: " + user_input)
