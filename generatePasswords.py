
file = open("passwords.txt", "w")

other = (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
other.extend(['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'])
other.extend(['t', 'u', 'v', 'w', 'x', 'y', 'z'])

passwords = []
for i in other:
    for j in other:
        for z in other:
            for n in other:
                newPassword = ""
                newPassword += i
                newPassword += j
                newPassword += z
                newPassword += n
                passwords.append(newPassword)
for i in passwords:
    file.write(i)
    file.write("\n")
file.close()