fish_record='鲨鱼1条、旗鱼2条、章鱼4条、金龙鱼2条'
#鲨鱼【0：2】，旗鱼【5：7】，章鱼【10：12】，金龙鱼【15：18】
print(len(fish_record))
b=1
while b<1000:
    a=input("请输入你要查找的品种：")
    
    if a=='鲨鱼':
        print(fish_record[0:4])
           
    elif a=='旗鱼':
        print(fish_record[5:8])
    elif a=='章鱼':
        print(fish_record[10:14])
    elif a=='金龙鱼':
        print(fish_record[15:20])
    else:
        print("Wrong Input")
    c=input("Shall we go on? [Y/N]:")
    if(c=='n'or c=='N'):
                break
b+=1
  

