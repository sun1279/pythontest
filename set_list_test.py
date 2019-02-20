list1=['apple', 'banana','peach','watermelon']
list2=['strawberry', 'watermelon']

s_list1=set(list1)
s_list2=set(list2)
print("s_list1=", end='')
print(s_list1)
print("s_list2=", end='')
print(s_list2)

print("Items in s_list1 DIFFERENT from items in s_list2 are:")
out = s_list1.difference(s_list2)
print(out)
print("Items in s_list2 DIFFERENT from items in s_list1 are:")
out = s_list2.difference(s_list1)
print(out)

print("Items in s_list1 SAME with items in s_list1 are:")
out = s_list1.intersection(s_list2)
print(out)
