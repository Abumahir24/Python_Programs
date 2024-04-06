#Appending elements to empty list
my_list=[]
elements=[10,20,30,40]
my_list.append(elements)
print("My list after apending is:", my_list)

#Insert the value 15 at the second position in the list
elements.insert(1,15)
print('My list after inserting 15:', my_list)

#Extending a my_list with another list:[50,60,70]
another_list=[50,60,70]
elements.extend(another_list)
print('After extending the list, my list:', my_list)

#Remove the last element from my_list:
del elements[7]
print('After removing last element from a list:', my_list)

#Sort my_list in ascending order.
my_list=[10,15,20,30,40,50,60]
sorted_list=sorted(my_list)
print('The sorted list in ascending:', my_list)

#Find and print the index of the value 30 in my_list.
my_lis=[10,15,20,30,40,50,60]
value=30
index=my_list.index(value)
print('The index of the value 30 is:', index)