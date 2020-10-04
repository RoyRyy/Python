import random
string = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
code=''
for i in range(4):
    num = random.randint(0,len(string)-1)
    code += string[num]
print(code)