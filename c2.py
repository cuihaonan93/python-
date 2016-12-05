origintext = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.\
 bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle.\
 sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
 '''

#origintext = origintext.split(" ")
print(origintext)
translatebook = "abcdefghijklmnopqrstuvwxyz"

result = ""
for j in origintext:
    first_place =  translatebook.find(j)
    #print( i , first_place)
    if first_place >= 0:
        second_place = first_place + 2
        if first_place > 23:
            second_place = first_place - 24
        result += (translatebook[second_place])
    else :
        result += j

print(result)
