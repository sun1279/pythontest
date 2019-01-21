#----------------RESULT-------------
#[4, 'm']
#['abc']
#[4, 'm']
#
#You may erroneously expect list1 to be equal to [10] and list3 to match with [隆庐a隆炉], thinking that the list argument will initialize to its default value of [] every time there is a call to the extendList.
#
#However, the flow is like that a new list gets created once after the function is defined. And the same get used whenever someone calls the extendList method without a list argument. It works like this because the calculation of expressions (in default arguments) occurs at the time of function definition, not during its invocation.
#
#The list1 and list3 are hence operating on the same default list, whereas list2 is running on a separate object that it has created on its own (by passing an empty list as the value of the list parameter).
def ListExtend(value, list=[]):
    list.append(value)
    return list

list1=ListExtend(4)
list2=ListExtend('abc',[])
list3=ListExtend('m')

print(list1)
print(list2)
print(list3)
