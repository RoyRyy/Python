#两种排序方法
#冒泡排序
print("冒泡排序：")
a=list(map(int,input("请输入数字，空格间隔: ").split()))
'''首先使用split()函数将输入根据空格转换为字符串的列表，
再使用map()函数将字符串列表中的每个字符串 ‘1’ 转化为int整型数值  1 ，
最后将map返回的对象转为数值列表a 最后列表中的便是需要的列表了'''
i=0
temp=0
while i<len(a):
    j=1
    while j<len(a)-i:
        if a[j]>a[j-1]:
            temp=a[j-1]
            a[j-1]=a[j]
            a[j]=temp
        j+=1
    i+=1
print("排序的结果从大到小为:")
print(a)
print("排序的结果从小到大为：")
a.reverse()
print(a)
print()
#用函数排序
print("用函数排序：")
b=list(map(int,input("请输入数字，空格间隔: ").split()))
print("排序的结果从小到大为：")
b.sort()
print(b)
print("排序的结果从大到小为：")
b.sort(reverse=True)
print(b)
print()


