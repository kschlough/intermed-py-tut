# freecodecamp - intermediate python programming course

# basic concepts review

# lists

# initialize
mylist = ['x', 'y', 'z']
mylist2 = list()

# access by index
mylist[0] 
mylist[-1]

# loop
for item in mylist:
    print(item)

# number of elements in list
length = len(mylist)

# append items
mylist.append('the alphabet is over')

# remove & return last item in the list
popped = mylist.pop()

# remove specific element
mylist.remove('x')

# remove all elements
mylist.clear()

# reverse the list
mylist.reverse()

# sort --> in place, changes original list
mylist.sort()

# sort --> and create new list, original is unchanged
new_list = sorted(mylist)

# new list with same element multiple times
mylist = [0] * 5
mylist2 = ['your intellectual superior'] * 2

# concat two lists
concat_lists = mylist + mylist2

# slice to access subparts of list
# list[startindex:stopindex:step] --> default step is 1

# from index 0 through 4 (not incl. 5)
concat_lists[:5]
# from index 2 through end (incl. 2)
concat_lists[2:]
# step through every other 
concat_lists[::2]
# negative index to reverse list
concat_lists[::-1]

