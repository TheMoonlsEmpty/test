# for i in range(1,10):
#    for j in range(i,10):
#        if i==j:
#           print(" "*7*(i-1),"%s*%d=%-2d" %(i,j,(i*j)) , end=" ")
#        else:
#            print("%s*%d=%-2d" % (i, j, (i * j)), end=" ")
#    print()
#
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end=' ')
    print()