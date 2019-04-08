'''
A set is unordered collection of items
Elements has to be unique
must be imutable
sets doesnt support indexing 
'''
l1 = []
l1 = list()
t1 = ()
t2 = 1, 2
t3 = 1,
t4 = tuple()

# create a set
my_Set = {1, 2, 3}
print(my_Set)

# mixed data types
my_Set = {1.0, "Hello", (11, 12, 13)}
print(my_Set)

my_Set = {1, 2, 3, 4, 3, 2}
print(my_Set)

# set can not comprise mutable types
my_Set = {1, 2, (34, 45)}
print(my_Set)

# Error on uncomment, since set can not have lists
# my_Set = {1, 2, [34, 45]}
# print(my_Set)

# ----------------------------------------
print("_" * 50)
print(type(my_Set))
my_Set = {}  # this is not a set, its a dictionary
print(type(my_Set))
# error on uncomment: since it doen't support indexing
# print(my_set[0])
my_Set = set()
print(type(my_Set))
print("_" * 50)
my_Set = {1, 3}
print(my_Set)
my_Set.add(2)
my_Set.add(5)
my_Set.add(4)
print(my_Set)
print("_" * 50)
my_Set.update([22, 33, 44])
print(my_Set)
print("_" * 50)
my_Set.update([222, 33, 444], {6, 7, 8})
print(my_Set)
print("_" * 50)
# discard : if any element doesnt exists in set, it will ignore
my_Set.discard(444)
my_Set.discard(333)
my_Set.discard(222)
print(my_Set)
print("_" * 50)
# discard : if any element doesnt exists in set, it will throw an exception
# remove:
my_Set.remove(4)
my_Set.remove(44)
# my_Set.remove(333)
print(my_Set)
print("_" * 50)
my_Set = set("sachin")
print(my_Set)
print(my_Set.pop())
print(my_Set)
print(my_Set.pop())
print(my_Set)
print(my_Set.pop())
print(my_Set)
print(my_Set.pop())
print(my_Set)

my_Set.clear()
print(my_Set)
