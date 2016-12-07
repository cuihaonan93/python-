import re

file_path ="D:\\Documents\\GitHub\\python\\channel\\"
number_file = "90052.txt"
def getdata(digit):
    path = file_path + digit
    global data
    data = open(path)
    data = data.readlines()[0]

i = 1
while i:
    getdata(number_file)
    digit = re.findall(r'\d+',data)
    if digit:
        digit = digit[len(digit)-1]
        number_file = "%s"%digit + ".txt"
        print(i,number_file)
        i += 1
    else:
        print(data)
        i = 0
