#lists

course = ["math", "physics","chemistry","comp sc", "biology"]
new_course = ["SSS101","PHE201","COM201"]
num_list = [1,3,4,5,6,7,8]


add_course = course.append("further mathematics") #the method 'append' adds to an existing list
insert_course = course.insert(0,"crs")
extend_course = course.extend(new_course)#the extend method adds two lists together
rem_course = course.remove("math") #the remove method removes an item from the list
popup = course.pop()#the pop method removes the last item from a list by default
rev_course = course.reverse()#the reverse method reverse a list
sorting = num_list.sort()#the sort method sorts the list
desc_sort = num_list.sort(reverse=True) #this method takes an argument and it reverse the list
sorted_num = sorted(num_list) #this can be use to sort a list by using the sorted function
minimum_list = min(num_list) #to check for min,max,sum in a list
index_finder = course.index("chemistry") #the index method finds the index of an item in a list
available_item = ('math' in course)#this checks through if an item is available or present in a list
course_string = ','.join(course) #this method converts a list into a string using the .join, ',' specifies the comma to seperate it
new_string = course_string.split(' - ') #the split method converts back to a string

print(num_list)
print(len(course)) #gets the length of the list
print(course[0:4]) #printing an index value or a range of items in a list
print(course[-1]) #the -1 usually print the last value in a list
print(course)
print(sorted_num)
print(minimum_list)
print(index_finder)
print(available_item)
print(course_string)
print(new_string)

#this explains how to print out a list with their number or index using the enumerate function, you can also
#specify the starting number
for index,items in enumerate(course, start=1):
    print(index,items)