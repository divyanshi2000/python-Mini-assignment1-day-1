"""Using filter() function filter the list so that only negative numbers are left."""

num=[82,24,-89, 78]
print ("numbers in the list:",num)
new_num= list(filter(lambda x: x<0,num))
print ("negative no",new_num)