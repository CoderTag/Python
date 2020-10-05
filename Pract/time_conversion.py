def timeConversion(s):
    s1 = s.split(':')
    if(s1[2].find('PM') >= 0):
        if(int(s1[0]) != 12):
            h = int(s1[0]) + 12
            s1[0] = str(h)

    if(s1[2].find('AM') >= 0):
        if(int(s1[0]) == 12):
            h = 0
            s1[0] = str(h)

    if (len(s1[0]) < 2):
        s1[0] = '0' + s1[0]

    s = ":".join(s1)
    s = s[:-2]
    return(s)


print(timeConversion('07:05:45PM'))
print(timeConversion('06:40:03AM'))
print(timeConversion('12:45:54PM'))
print(timeConversion('04:59:59AM'))
