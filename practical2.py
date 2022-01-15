# 20CE075 PARTH PARMAR
# Practical 2: Study and Learn List, Tuple, Set and Dictionary
# https://github.com/Morningstar000/Python-Practical-2


##### Dictionary #####


# a.Write a Python script to check whether a given key already exists in a dictionary.
def isKeyPresent(dict,key):
    if key in dict.keys():
        print("key is present in dictinary.")
    else:
        print("key is not present in dictionary.")

dict={'a':1,'b':2,'c':3}
key='c'
isKeyPresent(dict,key)

# b.Write a Python script to merge two Python dictionaries.
def dictmerg(dict1,dict2):
    resdict={}
    resdict.update(dict1)
    resdict.update(dict2)
    return resdict

dict1={'a':1,'b':2,'c':3}
dict2={1:'x',2:'y',3:'z'}
dict3=dictmerg(dict1,dict2)
print(dict3)

# c.Write a Python program to sum all the items in a dictionary.
def dictsum(dict1):
    sum=0
    for i in dict1:
        sum+=dict1[i]
    return sum
print(dictsum(dict1))

# d.Write a Python script to add a key to a dictionary.
def addkey(dict,key,value):
    dict[key]=value
    return dict
addkey(dict1,'d',4)
print(dict1)

# e.Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
def condict(dic1,dic2,dic3):
    dic4={}
    for i in (dic1,dic2,dic3):
        dic4.update(i)
    return dic4
print(condict(dic1,dic2,dic3))


##### Tuple #####


# a.Write a Python program to create a tuple with different data types.
tuple1=("extreme",2,True,2.1)
print(tuple1)

# b.Write a Python program to create a tuple with numbers and print one item.
tuple2=(1,2,3,4,5,6,7,8,9)
print(tuple2[5])

# c.Write a Python program to add an item in a tuple.
tuple2=(1,2,3,4,5,6,7,8,9)
def additemtotuple(tuplex,item):
    lst1=list(tuplex)
    lst1.append(item)
    tuplex=tuple(lst1)
    return tuplex
print(additemtotuple(tuple2,10))

# d.Write a Python program to convert a tuple to a string.
def tupletostring(tuplex):
    str1=''
    for i in tuplex:
        str1+=i
    return str1
tuple6 = ('a','b','c','d','e')
str6 = tupletostring(tuple6)
print(str6)

# e.Write a Python program to find the length of a tuple.
print(len(tuple6))
 #or
count=0
for i in tuple6:
    count+=1
print(count)


##### Set #####


#a. Write a Python program to add member(s) in a set and clear a set
set1={'p','a','r','t'}
set1.add('h')
print(set1)
set1.add((1,2,3))
print(set1)
set1.clear()
print(set1)

#b. Write a Python program to remove an item from a set if it is present in the set.
set1={'p','a','r','t'}
if 't' in set1:
    set1.remove('t')
print(set1)

#c. Write a Python program to create an intersection, Union, difference of sets.
a={25,26,47,66,28};
b={11,25,34,47,15};
print(a)
print(b)
print("intersection :", a & b)
print("union :", a | b)
print("difference :", a - b)

#d. Write a Python program to find maximum and the minimum value in a set.
set3 = {5, 29, 40, 15, 17, 69}
print(set3)
print("Maximum value :",max(set3))
print("Minimum value :",min(set3))

#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
    # for list
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num,counter
 
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

    # for Tuple
def most_frequent(tuple):
    counter = 0
    num = tuple[0]
    for i in tuple:
        curr_frequency = tuple.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num,counter
 
tuplev = (2, 1, 2, 2, 1, 3)
print(most_frequent(tuplev))

    # for dictionary
def most_frequentd(List):
    return max(set(List), key = List.count)
dict={1:11,2:22,3:33,4:11,5:11}
List = list(dict.values())
a=most_frequentd(List)
print(a,List.count(a))
