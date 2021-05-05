'''#program for squere program
l = input().split()
l_sqr = [int(i)*int(i) for i in l]
print(l_sqr)
---------------------------------------------------
# program for duplicate value
l1 = input().split()
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        print( i " is already in list")
print(l2)
'''
'''
------------------------------------------------------
L1 = [ '1' , '2' , '3' , '4' ]
L2 = [ '9' , '6' , '5' , '2' ]
for i in L1:
   if i in L2:
    print("true")
   else:
    print("false")
------------------------------------------------------
'''
L1 = [1,[2,3],[4,5,[6,7]]]
L2 = []
for i in L1:
    if type(i) is int:
        L2.append(i)
        continue
    elif i is list:
        for j in L1:
            L2 = L1.index(j)


print(L2)






