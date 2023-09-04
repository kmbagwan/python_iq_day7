#### DAY 7 ##############
#Example Que
#1 Create a dictionary to store information about a person (name, age, address).
"""person = {'name':'karishma','age':28,'add':'pune'}
print(person)""" 

#2 Add a new key-value pair to an existing dictionary
"""dict = {'key1':'book','key2':'horror'}
print("original dict:",dict)
dict['3'] = 'is'
dict['4'] = 'add'
print("updated:",dict)"""

#3 Create a set of unique numbers from a list of numbers
"""def unique_num(duplicate):
	uni_num_set = set(duplicate)
	uni_num_list = list(uni_num_set)
	return uni_num_list
dup_list = [1,2,4,3,6,2,1,6]
print(unique_num(dup_list))"""

#Practice Question
#1 Given two dictionaries, merge them into a single dictionary
"""def merge(d1,d2):
	res = {**d1,**d2}
	return res
d1 = {1:'aa',2:'bb'}
d2 = {3:'cc',4:'dd'}
d = merge(d1,d2)
print(d)"""

#2 Write a program that finds the most frequent element in a list
"""def most_frequent(list):
	counter = 0
	num = list[0]
	for i in list:
		current = list.count(i)
		if(current > counter):
			counter = current
			num = i
	return num
list = [2,6,7,2,9]
print(most_frequent(list))"""

#3 Implement a function that removes a key-value pair from a dictionary
"""dict1 = {1:"one",2:"two",3:"three",4:"four"}
print("Original dict: ",dict1)
del dict1[3]
print("dict after del: ",dict1)"""

#4 Create a program that checks if two sets have any elements in common
"""s1 = {1,2,3,4,9}
  s2 = {2,3,5,7,8}
  if s1.isdisjoint(s2):      #### isdisjoint() if the sets are disjoint meaning they have no elements in common
  	print("two sets No items in common")
  else:
  	print("two sets items in common")
  	print(s1.intersection(s2))    ### if sets are not disjoint meaning they sets have common elements"""  

#5 Given a list of dictionaries, find the dictionary with the highest value for a specific key
"""list_dict = [{"welcome": 8, "back":1, "code":9},
			{"welcome": 2, "back":9, "code":1},
			{"welcome": 5, "back":10, "code":7}]
print("the origonal list: " + str(list_dict))
res = {}
for dic in list_dict:
	for key,val in dic.items():
		if key in res:
			res[key] = max(res[key], val)
		else:
			res[key] = val
print("all highest value: " + str(res))"""

#6 Write a Python program that counts the number of occurrences of each character in a given string using a dict
"""inp_str = "gobabygo"
freq = {}
for i in inp_str:
	if i in freq:
		freq[i] += 1
	else:
		freq[i] = 1
print("Occurances of each character :\n " + str(freq))"""

#7 Given two sets, find the union, intersection, and difference between them
"""A = {1,8,4,7,9}
B = {1,4,9,0,8}
print("union :", A | B)
print("intersection :", A & B)
print("Difference :", A - B)"""

#8 Create a function that takes a list of dictionaries and sorts them based on a specified key
"""list = [{"subject":"english","std":5},
		{"subject":"history","std":9},
		{"subject":"geo","std":6}]
print("the list sorting by std :")
print(sorted(list, key=lambda i: i['std']))
print("\r")
print("the list sorting by subject and std :")
print(sorted(list, key=lambda i: (i['std'], i['subject'])))"""

#unsolved
#9 Write a program that finds the average value of all the elements in a list of dictionaries
"""list_dict = [{"abc":3, "is":2},{"alphabates":5}]
print("the original dict: " + str(list_dict))
res = 0
for val in list_dict.values():
	res += val
res = res / len(list_dict)
print("the average :" + str(res))"""


#10 Implement a function that takes a list of strings and returns a set of unique characters present in all strings.
"""def unique(str):
	s = set(str)
	return len(s)
if __name__ == "__main__":
	S = "uniquestring"
	print(unique(S))


S = "uniquestring"
a = ""
for i in S:
	if i not in a:
		a += i
print(len(a))"""

