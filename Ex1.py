from time import time

#! Set password
real_passwd = "5" * 15

#! Compare function
def compare(string1, string2):
    if len(string2) != len(string1):
        return False
    for i in range(len(string2)):
        if string2[i] != string1[i]:
            return False
    return True

#! timing attack to retrieve the length of the password
periods = []
for i in range(20):
    user_input = "x" * i
    begin = time()
    compare(real_passwd, user_input)
    end = time()
    period = end - begin
    periods.append(period)
length = periods.index(max(periods))
print(f"The length of the password is {length} characters")

#! timing attack to retrieve the password
characters_list = [chr(i) for i in range(128)]

for i in range(length):
    for character in characters_list:
        user_input = character
        begin = time()
        compare(real_passwd, user_input)
        end = time()
        period = end - begin
        periods.append(period)
    real_passwd += characters_list[periods.index(max(periods))]
print(real_passwd)
