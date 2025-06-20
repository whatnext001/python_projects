#Set
#they do throwaway duplicates, their values are unordered and no duplicates

course_set = {
    "History","biology","physics","mathematics","social studies"
}

advance_set = {
    "fmath", "COM 102","horticulture","aviation","dentist","biology"
}

combined_set = course_set.intersection(advance_set)#the intersection method works like a set interset
difference_set = course_set.difference(advance_set)
common_set = course_set.union(advance_set)


print(combined_set)
print(difference_set)
print(common_set)