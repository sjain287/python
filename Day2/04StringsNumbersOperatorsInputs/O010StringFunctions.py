team_name = "India"
player_name = "Sachin Tendulkar"
player_description = '''
Sachin the best ever in the history
He scored 100 centries
'''

print(team_name)
print(player_name)
print(player_description)

print(len(team_name))
print(team_name[0])
print(team_name[1])
print(team_name[-1])
print(team_name[-2])

# slicing
'''
Lower bound is inclusive
Upper bound is exclusive
'''
print("Slicing".center(50, "*"))
print(team_name[0:4])
print(team_name[2:4])
print(team_name[0:])
print(team_name[2:])
print(team_name[:3])
print(team_name[:])  # to copy a string

print("String API".center(50, "*"))
name = " SacHin TenDulkar "
print(name)
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip()+"sir")
print(name.lstrip()+"sir")
print(name.rstrip()+"sir")

print("_"*50)
print(id(name))  # id() -> gives memory address
name = name.strip().title()
print(type(name))
print(id(name))
print(name.find('a'))
name = "Mr."+name
print(id(name))
print("_"*50)

name = name[3:]
name1 = name
print(name.find('a'))
print(id(name))
print(id(name1))

print(name)
print(name1)
print("_"*50)
name = name+"sir"
print(id(name))
print(id(name1))
print("_"*50)

print("_"*50)
print(name)
print(name.find('a', 3))
print(name.find('kar'))
print(name.find('end'))
print(name.find('End'))  # -1 : seach is case sensitive
print(name.replace("Tend", "Tiger"))

print("_" * 50)
print('kar' in name)
print('man' in name)
print('mental' not in name)
