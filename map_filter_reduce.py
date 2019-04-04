from functools import reduce

mylist=[1,2,3,4,5]

#map applies a function to all the items in an input_list.
out=list(map(lambda x:x*2, mylist))
print(out)

#filter creates a list of elements for which a function returns true. it returns the original item of the list if True
out=list(filter(lambda x: x<4, mylist))
print(out)

#reduce keeps computing all the items in list, return the final result, NOT list
out=reduce(lambda x,y : x+y, mylist)
print(out)

#-------RESULT----------
#[2, 4, 6, 8, 10]
#[1, 2, 3]
#15
#
