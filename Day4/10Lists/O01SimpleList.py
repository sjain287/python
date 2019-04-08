'''
ways to create a list 
players = []
players=list()

list is a mutable type
'''
players1 = list()
players = []
print(type(players), type(players1))

players_india = ["sachin", "saurav", "rahul", "sehwag"]

print(players_india)

player_run = ["sachin", 153, ["sa", "aus", "wi"]]
print(len(players_india))
print(len(player_run))

print("_" * 30)

# Accessing list items
print(players_india)
print(players_india[1])
print(players_india[1:3])
print(players_india[-2])
print(id(players_india))
print(players_india)
print(id(players_india))
players_india[1] = "Ganguly"
print(players_india)
print(id(players_india))
players_india.append("Virat")  # append an element in the list
print(players_india)
print(id(players_india))

del players_india[2]
print(players_india)
print(id(players_india))


print("_" * 30)
my_list = list(range(10, 110, 10))
print(my_list)


my_char = list("Sachin Tendulkar")
print(my_char)
