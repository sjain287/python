players = ["Sachin", "Saurav", "Sehwag", "VVS", "Dhoni", "Kapil"]

for ply in players:
    print(ply)
print("_"*30)


for ply in players:
    print(ply)
    if (ply == "VVS"):
        break
    else:
        print("Next")
else:  # when loop completes, else runs, if loop breaks in between else part won't be executing
    print("Job completely done")


print("_" * 30)
success = True
for num in range(3):
    print(f'Attemp {num+1}')
    if (success):
        print("the job is over")
        break
else:
    print(f"all attemps done {num +1}")
