"""
Primitives
    numbers
    boolean
    Strings
"""
# let variables name be descriptive (Kent Beck)
players_count = 11
rating = 8.5
has_won_world_cup = True  # Boolean values are True and False and are case sensitive
team_name = "India"
print(players_count)
print(rating)
print(has_won_world_cup)
print(team_name)

# multiple assignments

a, b, c = 1, 2, "Hey"
print(a, b, c)

print(a, b, c)

first_name = "Sachin"
last_name = "Tendulkar"
print("My name is " + first_name + " I am also known as " + last_name)

'''
Identifiers Naming
    1.Case Sensitive
    2. do not use python keywords
'''

life_status = "Students"
spending_amount = 10000
print("*" * 40)
print(type(life_status))
print(type(spending_amount))

first_name = "Sachin"
last_name = "Tendulkar"
full_name = first_name + ' ' + last_name
print(full_name)

full_name = f'{first_name} {last_name} {5+4+2}'
print(full_name)
print(type(full_name))
