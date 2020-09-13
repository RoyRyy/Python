i=1
while i<=9:
    j=1
    while (j<=i):
        print('%d*%d=%-3d' % (i, j, i*j), end='\t')
        j+=1
    print('')
    i+=1