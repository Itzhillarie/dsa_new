#create an empty list of 10 items
My_List = [
[],
[],
[],
[],
[],
[],
[],
[],
[],
[]
]

#create a hash function that returns the unicode of char 
def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)
    return sum_of_char % 10

#insert a value into the hash table
def add(name):
    index = hash_function(name)
    My_List[index].append(name)
add("John")
add("Jane")
add("Jack")
add("Jill")
add("James")

#lookup a value in the hash table
def lookup(name):
    index = hash_function(name)
    if name in My_List[index]:
        return True
    else:
        return False

"""
def contains(name):
    index = hash_function(name)
    return my_list[index] == name

"""
print(lookup("John"))
print(My_List)
