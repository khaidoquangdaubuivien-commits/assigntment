def listcheck(list1):
    newlist = []
    for i in list1:
        if i % 2 ==0:
            newlist.append(i)
    return newlist
list1 = [1,2,3,4,5,6,7,8,9]
print(list1)
print(listcheck(list1))
