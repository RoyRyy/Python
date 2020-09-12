print('%1.2f'%(10.0/3))             #小数运算，结果为3.33
print((1-2j)*(2-3j))                #复数运算，结果为（-4-7j)
print(True and False)               #布尔运算，结果为False
print('%d'%(0b1110))                #二进制转化，结果为14
print(bin(14))                      #bin()函数把十进制数转化成二进制数
print(0b00110101&0b01100001)        #值为33，二进制为00100001
print(chr(0b00110101&0b01100001))   #chr(x)函数把x转为对应的ASCLL码字符，x为十进制数,把ASCLL码符转化为十进制数为ord
age1,age2,age3=10,9,0o12
print(age1==age3)                   #0o表示八进制，0o12结果为10，结果为True
print('a',ord('a'),bin(ord('a')),hex(ord('a')))   #a的十进制，二进制，十六进制数
print(bin(0b11^0b10))

