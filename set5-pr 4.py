l1 = [ '1' , '2' , '3' , '4' ]
l2 = [ '1' , '3' , '5' , '2' ]
for i in l1:
    if i in l2:
        print(i + " is in list 2")
    else:
        print(i + " is not in list 2")
